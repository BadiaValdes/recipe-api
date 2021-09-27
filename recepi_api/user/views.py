############ REST FRAMEWORK IMPORT ###########################
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics, filters
############ END REST FRAMEWORK IMPORT #######################

##########
from django.shortcuts import get_object_or_404
##########

########## My model
from .models import User
########## END My model

########## Serializer Class
from .serialize import UserSerializer, UserDetailsSerializer, UserDetailsAdminSerializer, UserPasswordChange, UserImageChange, UserImageBackgroundChange, UserCreateSerializer 
########## END Serializer Class

#class MultipleFieldLookupMixin:
#    """
#    Apply this mixin to any view or viewset to get multiple field filtering
#    based on a `lookup_fields` attribute, instead of the default single field filtering.
#    """
#    def get_object(self):
#        queryset = self.get_queryset()             # Get the base queryset
#        queryset = self.filter_queryset(queryset)  # Apply any filter backends
#        filter = {}
#        for field in self.lookup_fields:
#            if self.kwargs[field]: # Ignore empty fields.
#                filter[field] = self.kwargs[field]
#        obj = get_object_or_404(queryset, **filter)  # Lookup the object
#        self.check_object_permissions(self.request, obj)
#        return obj

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'username']
    

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    
class UserChangePassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserPasswordChange

class UserChangeAvatar(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserImageChange

class UserChangeBackground(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserImageBackgroundChange

class UserDatailAdmin(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserDetailsAdminSerializer

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
    
    
    
    
    

