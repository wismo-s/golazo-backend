from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serialisers import CreateUserSerializer, UserSerilizer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serialisers import TokenPairSerializer
# Create your views here.
MODEL_USER = get_user_model()
class CreateUserView(APIView):
    def post(self, request):
        serialiser = CreateUserSerializer(data = request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'response': 'user register'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'user not be crated'}, status=status.HTTP_400_BAD_REQUEST)
    
class Login(TokenObtainPairView):
    serializer_class = TokenPairSerializer

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user_serilizer = UserSerilizer(user)
                return Response({
                    'token': serializer.validated_data.get('access'),
                    'refresh-token': serializer.validated_data.get('refresh'),
                    'user': user_serilizer.data,
                    'message': 'session good!'
                }, status=status.HTTP_202_ACCEPTED)
            return Response({'error': 'user or password is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'user or password is not valid'}, status=status.HTTP_400_BAD_REQUEST)
    
class Logout(GenericAPIView):
    def post(self, request):
        user_obtain = request.data.get('user')
        user = MODEL_USER.objects.filter(id=user_obtain)
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'response': 'user logout'}, status=status.HTTP_200_OK)
        return Response({'error': 'user not exists'}, status=status.HTTP_400_BAD_REQUEST)