from db.serializers.instructor_course import CourseSerializer
from db.models.course import Course
from lib.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, instructor_id):
        try:
            queryset = Course.objects.filter(instructor_id=instructor_id).order_by('-created_at')
            instructor_courses=CourseSerializer(queryset,many=True)
            return Response({'courses':instructor_courses.data,'total': queryset.count()} )
        except Exception:
            return Response(None,{'message':'user does not exist'})
