from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, perfil_image, password=None):
        if not username:
            raise ValueError('username is nesesary')
        if not email:
            raise ValueError('email is nesesary')
        if not password:
            raise ValueError
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, perfil_image=perfil_image)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, email, perfil_image, password=None):
        if not username:
            raise ValueError('username is nesesary')
        if not email:
            raise ValueError('email is nesesary')
        if not password:
            raise ValueError('password is nesesary')
        email= self.normalize_email(email)
        user = self.model(username=username, email=email, perfil_image=perfil_image)
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=250, blank=False, null=False, unique=True)
    email = models.EmailField()
    is_superuser = models.BooleanField(default=False, blank=False, null=False)
    perfil_image = models.CharField(max_length=300, blank=False, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
    
    
    USERNAME_FIELD = 'username'
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'