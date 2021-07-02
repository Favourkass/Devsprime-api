from django.http import Http404
from rest_framework import  status
from rest_framework.views import APIView

from lib.response import Response
from db.models.course import Course
from api.permissions.is_course_author import IsAuthorOrReadOnly
from db.serializers.instructor_course import CourseSerializer




class CourseDetails(APIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)

        return Response(data={'course': serializer.data},status=status.HTTP_200_OK)

    def put(self, request, pk, **kwargs):
        update_course = self.get_object(pk)
        serializer = CourseSerializer(data=request.data, partial=True)
        self.check_object_permissions(request,update_course)
        if serializer.is_valid():
            serializer.instance = update_course
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        update_course = self.get_object(pk)
        update_course.delete()
        return Response(data={'data':{}},status=status.HTTP_204_NO_CONTENT)
   