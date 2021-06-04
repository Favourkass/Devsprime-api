from django.contrib.auth import authenticate
from rest_framework import status, response
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from db.serializers.login_serializer import LoginSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email == '' and password:
            data = {'message': "failure", 'data': 'null',
                    'errors': {'email': 'This field cannot be blank'}, }
            return response.Response(data, status=status.HTTP_401_UNAUTHORIZED)
        elif password == '' and email:
            data = {'message': "failure", 'data': 'null',
                    'errors': {'password': 'This field cannot be blank'}, }
            return response.Response(data, status=status.HTTP_401_UNAUTHORIZED)
        elif email == '' and password == '':
            data = {'message': "failure", 'data': 'null',
                    'errors': {'email': 'This field cannot be blank', 'password': 'This field cannot be blank'}, }
            return response.Response(data, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(email=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            token, _ = Token.objects.get_or_create(user=user)
            data = {'message': 'success', 'data': {
                'token': token.key}, 'errors': 'null', }

            return response.Response(data, status=status.HTTP_200_OK)

        data = {'message': "failure", 'data': 'null',
                'errors': 'Invalid credentials. Try again', }
        return response.Response(data, status=status.HTTP_401_UNAUTHORIZED)
