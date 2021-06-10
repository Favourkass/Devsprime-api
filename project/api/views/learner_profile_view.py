from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from lib.response import Response
from rest_framework.views import APIView
from db.models.learner import LearnerProfile
from db.models.learner import User
from db.serializers.learner_profile_serializer import LearnerProfileSerializer
from db.serializers.learner_profile_serializer import UserProfileSerializer


class LearnerProfileView(APIView) :
    serializer_class = LearnerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request) :
        user_in_learner = LearnerProfile.objects.get(user_id=request.user.id)
        if user_in_learner is not None:
            serializer = LearnerProfileSerializer(user_in_learner)
            return Response(dict(data=serializer.data))
        else:
            return Response(dict(data=serializer.data))
        
    def put(self, request, format=None) :
        user_in_learner = LearnerProfile.objects.get(user_id=request.user.id)
        serializer = LearnerProfileSerializer(user_in_learner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(dict(data=serializer.data))
        return Response(dict(data=serializer.data))


class UserProfileView(APIView) :
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request) :
        current_user_in_user = User.objects.get(id=request.user.id)
        serializer = UserProfileSerializer(current_user_in_user)
        return Response(dict(data=serializer.data))

    def put(self, request, format=None):
        current_user_in_user = User.objects.get(id=request.user.id)
        serializer = UserProfileSerializer(current_user_in_user, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(data=serializer.data)
        return Response(dict(data=serializer.data))
    
        
