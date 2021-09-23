from rest_framework import serializers
from .models import User

from django.contrib.auth.password_validation import validate_password

import os

from filecmp import dircmp

# With serializer.Model, like formModel
class UserSerializer (serializers.ModelSerializer):
    #recipe = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())

    class Meta:
        model = User
        fields = "__all__"

class UserDetailsSerializer (serializers.ModelSerializer):
    
    #recipe = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name','email','date_joined','avatar','groups', 'background_image', 'is_active','is_staff']
        read_only_fields=['avatar','background_image', 'is_active','is_staff']

class UserDetailsAdminSerializer (serializers.ModelSerializer):
    
    #recipe = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'username','email', 'last_login','date_joined','avatar','groups', 'is_active','is_staff','is_superuser']
        read_only_fields=['avatar','id', 'username']

class UserPasswordChange(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password]) # New Password
    password2 = serializers.CharField(write_only=True, required=True) # Confirmation
    old_password = serializers.CharField(write_only=True, required=True) # Old One
    
    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2') # Same as before
        
    def validate(self, attrs):
    	# attrs are the one decleared above
       if attrs['password'] != attrs['password2']:
           raise serializers.ValidationError({"password": "Password fields didn't match."}) # No Equals
       return attrs

    # Old password the same
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    # Make the update request
    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

class UserImageChange(serializers.ModelSerializer):
    avatar = serializers.ImageField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields=['avatar']
    
    def update(self, instance, validated_data):    
        if os.path.basename(instance.avatar.path) != 'avatar.png':
           instance.avatar.delete(save=True)
        instance.avatar = validated_data['avatar']
        instance.save()
        return instance
        
class UserImageBackgroundChange(serializers.ModelSerializer):
    background_image = serializers.ImageField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields=['background_image']
    
    def update(self, instance, validated_data):    
        
        instance.background_image.delete(save=True)
        instance.background_image = validated_data['background_image']
        instance.save()
        return instance

