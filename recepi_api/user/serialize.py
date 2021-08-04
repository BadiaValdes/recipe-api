from rest_framework import serializers
from .models import User


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
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name','email','date_joined','avatar','groups']

