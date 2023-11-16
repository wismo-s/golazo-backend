from django.urls import path
from .views import TshirtView, ListallCloth
urlpatterns = [
    path('tshirt/<slug:pk>', TshirtView.as_view(), name='tshirt'),
    path('items/<slug:pk>',  ListallCloth.as_view(), name='cloth_list')
]
