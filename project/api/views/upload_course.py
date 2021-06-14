from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from db.models.course import Course
from db.models.instructors import Instructor
from db.serializers.upload_course import UploadCourseSerializer
from api.permissions.upload_course import IsInstructor
from api.utils import Util
from lib.response import Response

import cloudinary.uploader


class UploadCourseView(APIView):
    parser_classes = (MultiPartParser, JSONParser, FormParser)
    permission_classes = (permissions.IsAuthenticated, IsInstructor,)
    serializer_class = UploadCourseSerializer

    def post(self, request):
        instructor = Instructor.objects.get(user_id=request.user)
        serializer = UploadCourseSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid(raise_exception=True):
            cover_img = serializer.validated_data['cover_img']
            overview = serializer.validated_data['overview']
            videos = serializer.validated_data['course_url']

            course_video_uploads_have_valid_formats = all(
                [Util.validate_video_upload(video) for video in videos])
            overview_video_has_valid_format = Util.validate_video_upload(
                overview)
            cover_image_has_valid_format = Util.validate_image_upload(
                cover_img)

            if course_video_uploads_have_valid_formats and overview_video_has_valid_format and cover_image_has_valid_format:
                title = serializer.validated_data['title']
                description = serializer.validated_data['description']
                price = serializer.validated_data['price']
                category_id = serializer.validated_data['category_id']
                type_id = serializer.validated_data['type_id']

                # UPLOAD VALIDATED FILES TO CLOUDINARY
                uploaded_cover_img = cloudinary.uploader.upload(
                    cover_img, folder=f'Courses/{title}', use_filename=True, overwrite=True, unique_filename=False)

                uploaded_overview = cloudinary.uploader.upload_large(
                    overview, folder=f'Courses/{title}', use_filename=True, overwrite=True, unique_filename=False, resource_type="video")

                url_list = []
                for video in videos:
                    uploaded_video = cloudinary.uploader.upload_large(
                        video, folder=f'Courses/{title}/courses', use_filename=True, overwrite=True, unique_filename=False, resource_type="video")
                    url_list.append(uploaded_video['url'])

                # CREATE COURSE AND PERSIST INTO DATABASE
                course = Course.objects.create(title=title, description=description, price=price, category_id=category_id, type_id=type_id, instructor_id=instructor,
                                               cover_img=uploaded_cover_img['url'], overview=uploaded_overview['url'],
                                               course_url=url_list)
                course.save()
                data = {}
                data['instructor_id'] = instructor.id
                data['cover_img'] = uploaded_cover_img['url']
                data['overview'] = uploaded_overview['url']
                data['course_url'] = url_list
                data['created_at'] = course.created_at
                data['updated_at'] = course.updated_at

                response_data = {**{'Id': course.id},
                                 **serializer.data, **data}
                return Response(data=response_data, status=status.HTTP_201_CREATED)
        return Response(errors={'format_error': 'cover_img must have image format, overview must have video format and course_url can only accept video format for file(s)'}, status=status.HTTP_400_BAD_REQUEST)
