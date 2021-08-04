from rest_framework.response import Response

from .models import User
from rest_framework import generics

from .serialize import UserSerializer, UserDetailsSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    
    
    
    
    
    

