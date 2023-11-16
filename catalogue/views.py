from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .scraper import catalogScraper
# Create your views here.
class TshirtView(APIView):
    def get(self, request, pk):
        
        """
        parameters---> polos-deportivos-hombre, polos-oversize
        """
        
        api_content = catalogScraper(url=pk, html_class='lazyloaded', includ='|')
        return Response(api_content, status=status.HTTP_200_OK)

class ListallCloth(APIView):  
    def get(self, request, pk):
        
        """
        parameters---> sets-deportivos-mujer, leggings, sport-bras, biker-shorts, bodysuits, polos-oversize-de-mujer, polos-de-mujer, accesorios, sale, shorts-deportivos-hombre, cortavientos-impermeables-hombre, joggers-hombre, bividis-deportivos-hombre, gorras
        """
        
        api_content = catalogScraper(url=pk, html_class='grid-product__image lazyloaded', includ='-')
        return Response(api_content, status=status.HTTP_200_OK)