from lib.response import Response
from rest_framework import status
from rest_framework.views import APIView
from db.models.course import Course
from db.serializers.instructor_course import CourseSerializer


class AllCourses(APIView):
    '''Display all available courses'''

    serializer_class = CourseSerializer

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(data={'courses': serializer.data}, status=status.HTTP_200_OK)
        