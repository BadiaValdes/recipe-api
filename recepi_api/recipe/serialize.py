from rest_framework import serializers
from recipe.models import Category, Product, Difficulty, Ingredient, UserLike, Measurement, Recipe, RecipeImage

from django.http import HttpResponse

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
        
class IngredientSerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = Ingredient
        fields = ['id', 'fk_recipe', 'fk_product', 'fk_measurement_unit', 'main_ingredient', 'amount']

class RecipeSerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    # fk_difficult = DifficultySerializer(many=False) # Nested JSON serializer
    # fk_category = CategorySerializer(many=False) # Nested JSON serializer
    recipe_ingredient = serializers.StringRelatedField(many=True) # __str__ nested serialize with other model that has a relationship with this one
    #recipe_ingredient = IngredientSerializer(many=True)
    fk_difficult = serializers.StringRelatedField(many=False)  # __str__ nested serialize
    fk_category = serializers.StringRelatedField(many=False)  # __str__ nested serialize

    # fk_user = serializers.StringRelatedField(many=False) # __str__ nested serialize

    class Meta:
        model = Recipe
        lookup_field = 'slug'
        fields = ['id', 'slug', 'name', 'img', 'description', 'fk_difficult', 'fk_category', 'steps', 'recipe_ingredient', 'fk_user']

class IngredientSerializer(serializers.ModelSerializer):
    # Everything must be inside of the meta class
    class Meta:
        model = Ingredient
        fields = ['id', 'fk_recipe', 'fk_product', 'fk_measurement_unit', 'main_ingredient', 'amount']

class RecipeSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'slug', 'name', 'img', 'description', 'fk_difficult', 'fk_category', 'steps','fk_user']

    def create(self, validated_data):
        ingredients = validated_data.pop('recipe_ingredient')
        recipe = Recipe.objects.create(**validated_data)
        print(ingredients)
        mainOne = False;
        for i in ingredients:
            measurement = Measurement.objects.get(id=i['measurement'])
            print("Measuremnt")
            print(measurement)
            product = Product.objects.get(id=i['product'])
            print("Product")
            print(product)
            if i['principal']:
                mainOne = True
            else:
                mainOne = False
            Ingredient.objects.create(main_ingredient=mainOne,
                                      amount=i['cantidad'],
                                      fk_measurement_unit_id=measurement.id,
                                      fk_product_id=product.id,
                                      fk_recipe_id=recipe.id )
            print(i['product'])
        print("pase por aqui")

    #
    #       recipe = Recipe.objects.create(**validated_data)
    #       #Ingredient.objects.create(fk_recipe=recipe, **ingredients)
        return HttpResponse({'message': 'Recipe Created'}, status=200)




class ReciepeImageSerialize(serializers.ModelSerializer):
    class Meta:
        model = RecipeImage
        fields = ['image']
