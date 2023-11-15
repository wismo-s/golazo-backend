from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from bs4 import BeautifulSoup
from rest_framework import status
import requests as resq
URL_BASE = 'https://www.alphafit.pe/collections/polos-oversize'

"""
        cloth_divs = soup.find_all('div', class_='grid-product__title grid-product__title--body')
        for cloth in cloth_divs: 
            print(cloth.text)
"""

# Create your views here.
class TshirtView(APIView):
    def get(self, request):
        obtain_request = resq.get(URL_BASE)
        html_result = obtain_request.text 
        
        soup = BeautifulSoup(html_result, "html.parser")
        images_divs = soup.find_all('img', class_="lazyloaded")
        api_content = []
        count = 0
        for img in images_divs:
            if "|" in img['alt']:
                obj = { 'id': count, 'title': img['alt'], 'img': img['src']}
                count+=1
                api_content.append(obj)
        return Response(api_content, status=status.HTTP_200_OK)