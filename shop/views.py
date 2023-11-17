from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import FactureSerializer
from .models import Facture
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
# Create your views here.
USER_MODEL = get_user_model()
class FactureViewSets(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serialiser = FactureSerializer(data=request.data) 
        if serialiser.is_valid():
            userid = USER_MODEL.objects.get(id=serialiser.data['user_id'])
            facture = Facture.objects.create(user_id=userid, products=serialiser.data['products'] , total=serialiser.data['total'])
            facture.save()
            print(userid.id)
            return Response({'response':'godd'}, status=status.HTTP_200_OK)
        return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        factures=Facture.objects.filter(user_id=pk)
        if factures:
            serialiser = FactureSerializer(factures, many=True)
            return Response(serialiser.data, status=status.HTTP_200_OK)
        return Response({'response': 'bad'}, status=status.HTTP_400_BAD_REQUEST)
