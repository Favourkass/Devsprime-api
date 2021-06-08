from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from lib.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from db.models.instructors import Instructor
from db.models.user import User
from db.serializers.instructor_profile_seriaizer import InstructorProfileSerializer
from api.permissions.instructor import IsInstructor



class InstructorProfile(APIView):
    permission_classes = [IsAuthenticated & IsInstructor]
    serializer_class = InstructorProfileSerializer

    def get(self, request):
        instructor = Instructor.objects.filter(user_id=request.user.id)
        if not instructor:
            return Response(errors={"invalid_user": "User is not an instructor"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = InstructorProfileSerializer(instructor[0])
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        
    def put(self, request,format=None):
        instructor = Instructor.objects.get(user_id=request.user.id)
        serializer = InstructorProfileSerializer(instructor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

