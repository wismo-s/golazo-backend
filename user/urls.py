from django.urls import path
from .views import CreateUserViewSet, EditUserViewSet
from .views import Login, Logout
urlpatterns = [
    path('create/', CreateUserViewSet.as_view(), name='singin'),
    path('edit/', EditUserViewSet.as_view(), name='edit'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
