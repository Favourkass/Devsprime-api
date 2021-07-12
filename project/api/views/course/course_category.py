from db.serializers.course_category_serializer import CourseCategorySerializer
from db.models.course_category import CourseCategory
from lib.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CourseCategoryListView(APIView):
    '''Display all course category available'''

    def get(self, request):
        qs = CourseCategory.objects.all()
        serializer = CourseCategorySerializer(qs, many=True)
        return Response(data={'course_categories': serializer.data}, status=status.HTTP_200_OK)
        
    def post(self,request):
        serializer = CourseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)