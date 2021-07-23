import cloudinary.uploader
from django.http import Http404
from rest_framework import views, status, permissions
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from api.utils import Util
from lib.response import Response
from db.models.course import Course
from db.models.course_video import CourseVideo
from api.permissions.is_course_author import IsAuthorOrReadOnly
from db.serializers.course_video_serializer import CourseVideoSerializer, UploadCourseVideoSerializer


class CourseVideoList(views.APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_classes = CourseVideoSerializer
    parser_classes = (MultiPartParser, JSONParser, FormParser)

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        course_videos = CourseVideo.objects.filter(course_id=course)
        serializer = CourseVideoSerializer(course_videos, many=True)
        course_info = dict()
        course_info['title'] = course.title
        course_info['price'] = course.price
        course_info['cover_img'] = course.cover_img
        course_info['description'] = course.description
        return Response(dict(**course_info, videos=serializer.data, total=len(serializer.data)), status=status.HTTP_200_OK)

    def post(self, request, pk):
        course = self.get_object(pk=pk)
        self.check_object_permissions(request, course)
        data = request.data
        data['course_id'] = course.id
        serializer = UploadCourseVideoSerializer(data=data)
        if not serializer.is_valid():
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # CHECK VIDEO FILE FORMAT
        videos = serializer.validated_data['video_urls']
        is_videos_valid = all(
            [Util.validate_video_upload(video) for video in videos])
        if not is_videos_valid:
            return Response(errors=dict(invalid_video='Please upload a valid video format'))

        # UPLOAD COURSE TO CLOUDINARY
        title = course.title
        for video in videos:
            uploaded_video = cloudinary.uploader.upload_large(
                video, folder=f'Courses/{title}/courses', use_filename=True, overwrite=True, unique_filename=False, resource_type="video")

            # SAVE COURSE VIDEO TO DB
            CourseVideo.objects.update_or_create(
                course_id=course,
                name=uploaded_video['original_filename'],
                video_url=uploaded_video['url']
            )

        # RESPONSE DATA
        res_data = dict()
        res_data['title'] = title
        res_data['course_id'] = course.id
        res_data['instructor name'] = course.instructor_id.user_id.fullname
        course_videos = CourseVideo.objects.filter(course_id=course)
        output_serializer = CourseVideoSerializer(course_videos, many=True)
        res_data['videos'] = output_serializer.data

        return Response(data=res_data, status=status.HTTP_201_CREATED)
