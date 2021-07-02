from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from db.models.course import Course
from db.models.instructors import Instructor
from db.models.course_video import CourseVideo
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

            is_course_video_valid = all(
                [Util.validate_video_upload(video) for video in videos])
            is_overview_video_valid = Util.validate_video_upload(
                overview)
            is_cover_img_valid = Util.validate_image_upload(
                cover_img)

            if is_course_video_valid and is_overview_video_valid and is_cover_img_valid:
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

                # CREATE COURSE AND PERSIST INTO DATABASE
                course = Course.objects.create(title=title, description=description, price=price, category_id=category_id, type_id=type_id, instructor_id=instructor,
                                               cover_img=uploaded_cover_img['url'], overview=uploaded_overview['url'],
                                            )
                
                course.save()
                # Create Course Video                               
                for video in videos:
                    uploaded_video = cloudinary.uploader.upload_large(video, folder=f'Courses/{title}/courses', use_filename=True, overwrite=True, unique_filename=False, resource_type="video")
                    
                    course_video = CourseVideo.objects.create(
                        course_id=course,
                        name=uploaded_video['original_filename'],
                        video_url=uploaded_video['url']
                    )
                    course_video.save()
    
                # Response Data
                data = {}
                data['instructor_id'] = instructor.id
                data['cover_img'] = uploaded_cover_img['url']
                data['overview'] = uploaded_overview['url']
                data['created_at'] = course.created_at
                data['updated_at'] = course.updated_at

                response_data = {**{'Id': course.id},
                                 **serializer.data, **data}
                return Response(data=response_data, status=status.HTTP_201_CREATED)
        return Response(errors={'format_error': 'cover_img must have image format, overview must have video format and course_url can only accept video format for file(s)'}, status=status.HTTP_400_BAD_REQUEST)
