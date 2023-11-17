from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

USER_MODEL = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ['username', 'email', 'perfil_image', 'password']
        
    def create(self, data):
        user = USER_MODEL.objects.create_user(username=data['username'], email=data['email'], perfil_image=data['perfil_image'], password=data['password'])
        user.save()
        return user
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ['id', 'username', 'email', 'perfil_image', 'first_name', 'last_name', 'direccion', 'gender', 'phone']
        
class EditSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)
    perfil_image = serializers.CharField(max_length=300, required=False)
    password = serializers.CharField(max_length=128)
    first_name = serializers.CharField(allow_blank=True, max_length=150, required=False)
    last_name = serializers.CharField(allow_blank=True, max_length=150, required=False)
    direccion = serializers.CharField(allow_blank=True, max_length=300, required=False)
    gender = serializers.CharField(allow_blank=True, required=False)
    phone = serializers.CharField(allow_blank=True, max_length=9, required=False)
    
class TokenPairSerializer(TokenObtainPairSerializer):
    pass