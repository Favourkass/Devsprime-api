from rest_framework import generics, permissions, authentication, status, mixins
from lib.response import Response
from lib.card_validator import card_validator
from db.models.learner import LearnerProfile
from api.serializers.serializers import LearnerCardSerializer


class LearnerCardView(
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView
):
    '''
    This viewset generates the endpoint for:
    card creation, reading update and delete 
    '''
    permission_classes = (permissions.IsAuthenticated,) 
    authentication_classes = [authentication.SessionAuthentication, 
                                authentication.TokenAuthentication,
                                authentication.BasicAuthentication]
    serializer_class = LearnerCardSerializer
    queryset = LearnerProfile.objects.all()
   
    def get(self, request, *args, **kwargs):        
        get_queryset = LearnerProfile.objects.get(user_id=request.user)
        response = {
            'account_name': get_queryset.account_name,
            'account_number': get_queryset.account_number,
            'bank_name': get_queryset.bank_name
        }
        return Response(response)

    def post(self, request, *args, **kwargs):
        get_queryset = LearnerProfile.objects.get(user_id=request.user)
        serializer = LearnerCardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return card_validator(self, get_queryset, serializer)
        return Response(None, {'Invalid request': 'Please enter valid data'})

    def put(self, request, *args, **kwargs):
        get_queryset = LearnerProfile.objects.get(user_id=request.user)
        serializer = LearnerCardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return card_validator(self, get_queryset, serializer)
        return Response(None, {'Invalid request': 'Please enter valid data'})    
    
    def delete(self, request, *args, **kwargs):
        get_queryset = LearnerProfile.objects.get(user_id=request.user)
        get_queryset.account_name = None
        get_queryset.account_number = None
        get_queryset.bank_name = None
        get_queryset.save()
        return Response({'card details': 'deleted successfully'})
