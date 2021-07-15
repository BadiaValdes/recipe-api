from rest_framework import serializers
from .models import Category, Product, Difficulty, Ingredient, UserLike, Measurement, Recipe


# Is like a django form

# class CategorySerializer(serializers.Serializer):
#     #### Fields that will be serialized ###
#     id = serializers.IntegerField(read_only=True)
#     slug = serializers.CharField(required=False, allow_blank=False, max_length=25)
#     name = serializers.CharField(required=False, allow_blank=False, max_length=20)
#
#     #######################################
#
#     def create(self, validated_data):
#         """
#         Do something here
#         :param validated_data:
#         :return:
#         """
#         print(validated_data)
#         return Category.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

# With serializer.Model, like formModel
class CategorySerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = Category
        fields = ['id', 'slug', 'name']


class ProductSerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = Product
        fields = ['id', 'slug', 'name']


class DifficultySerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = Difficulty
        fields = ['id', 'slug', 'name']

class MeasurementSerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = Measurement
        fields = ['id', 'slug', 'name']


class UserLikeSerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = UserLike
        fields = ['id', 'fk_recipe', 'fk_user']


class RecipeSerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = Recipe
        fields = ['id', 'slug', 'name', 'img', 'description', 'fk_difficult', 'fk_category', 'steps']


class IngredientSerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = Ingredient
        fields = ['id', 'fk_recipe', 'fk_product', 'fk_measurement_unit', 'main_ingredient', 'amount']