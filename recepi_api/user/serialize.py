from rest_framework import serializers
from .models import User


# With serializer.Model, like formModel
class UserSerializer (serializers.ModelSerializer):
    #recipe = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())

    class Meta:
        model = User
        fields = "__all__"
