from django.contrib.auth import get_user_model
from rest_framework import serializers
USER_MODEL = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ['username', 'email', 'perfil_image', 'password']
        
    def create(self, data):
        user = USER_MODEL.objects.create_user(username=data['username'], email=data['email'], perfil_image=data['perfil_image'], password=data['password'])
        user.save()
        return user