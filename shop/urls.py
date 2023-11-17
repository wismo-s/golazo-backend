from django.urls import path
from .views import FactureViewSets
urlpatterns = [
    path('factures/<int:pk>/', FactureViewSets.as_view(), name='facture')
]
