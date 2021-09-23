############ REST FRAMEWORK IMPORT ###########################
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics
############ END REST FRAMEWORK IMPORT #######################

########## My model
from .models import User
########## END My model

########## Serializer Class
from .serialize import UserSerializer, UserDetailsSerializer, UserDetailsAdminSerializer, UserPasswordChange, UserImageChange, UserImageBackgroundChange
########## END Serializer Class

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    
class UserChangePassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class = UserPasswordChange

class UserChangeAvatar(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class = UserImageChange

class UserChangeBackground(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class = UserImageBackgroundChange

class UserDatailAdmin(generics.RetrieveUpdateAPIView):
    permission_classes=[IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserDetailsAdminSerializer
    
    
    
    
    
    

