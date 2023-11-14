from django.urls import path
from .views import CreateUserViewSet
from .views import Login, Logout
urlpatterns = [
    path('create/', CreateUserViewSet.as_view(), name='singin'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
