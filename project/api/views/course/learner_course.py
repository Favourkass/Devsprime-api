from db.serializers.instructor_course import CourseSerializer
from db.models.learner_course import LearnerCourse
from db.models.learner import LearnerProfile
from db.serializers.learner_course_serializer import LearnerCourseSerializer
from rest_framework import permissions,views,status
from lib.response import Response


class LearnerCourseList(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        
        user = request.user.id
        name = request.user.fullname
        learner_id = LearnerProfile.objects.filter(user_id=user)
        if not learner_id:
            return Response(errors=dict(invalid_user="only learner can have a course"), status=status.HTTP_400_BAD_REQUEST)
        learner_id=learner_id.get().id
        learncourse = LearnerCourse.objects.filter(learner_id=learner_id)
        
        courses = [
            {
                'title': course.course_id.title, 
                'description': course.course_id.description,
                'course_url': course.course_id.course_url,
                'cover_img': course.course_id.cover_img,
                'instructor_name': course.course_id.instructor_id.user_id.fullname,
                'course_type': course.course_id.type_id.name,
                'course_category': course.course_id.category_id.name,
            }
             for course in learncourse ]

        response = {"fullname":name,
                    "courses":courses}        
        return Response(data=response, status=status.HTTP_200_OK)
        
