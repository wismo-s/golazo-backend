from django.urls import path
from .views import TshirtView
urlpatterns = [
    path('tshirt/', TshirtView.as_view(), name='tshirt')
]
