from db.serializers.course_type_serializer import CourseTypeSerializer
from db.models.course_type import CourseType
from lib.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CourseTypeListView(APIView):
    '''Display all course types available'''

    def get(self, request):
        course_types = CourseType.objects.all()
        serializer = CourseTypeSerializer(course_types, many=True)
        return Response(data={'course_types': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)