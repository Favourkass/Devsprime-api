from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from lib.response import Response
from rest_framework.views import APIView
from db.models.learner import LearnerProfile
from db.models.learner import User
from db.serializers.learner_profile_serializer import LearnerSerializer


class LearnerProfile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LearnerSerializer
    
    def get(self, request):
        current_user = User.objects.get(id=request.user.id)
        if not current_user.is_learner:
            return Response(errors=dict(invalid_user='This user is not a learner'), status=status.HTTP_400_BAD_REQUEST)
        serializer = LearnerSerializer(current_user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        current_user = User.objects.get(id=request.user.id)
        serializer = LearnerSerializer(current_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
