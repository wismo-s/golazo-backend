from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers import CreateUserSerializer
from rest_framework import status
# Create your views here.
class CreateUserView(APIView):
    def post(self, request):
        serialiser = CreateUserSerializer(data = request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'response': 'user register'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'user not be crated'}, status=status.HTTP_400_BAD_REQUEST)
