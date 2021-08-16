from rest_framework import serializers
from recipe.models import Category, Product, Difficulty, Ingredient, UserLike, Measurement, Recipe, RecipeImage

from django.http import HttpResponse

import json

# this part is important for object's CRUD

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
        model = Category # Model
        fields = ['id', 'slug', 'name'] # Fields to show


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
    recipe_ingredient = serializers.StringRelatedField(many=True, read_only=True) # __str__ nested serialize with other model that has a relationship with this one
    #recipe_ingredient = IngredientSerializer(many=True)
    fk_difficult = serializers.StringRelatedField(many=False)  # __str__ nested serialize
    fk_category = serializers.StringRelatedField(many=False)  # __str__ nested serialize

    # fk_user = serializers.StringRelatedField(many=False) # __str__ nested serialize

    class Meta:
        model = Recipe
        lookup_field = 'slug'
        fields = ['id', 'slug', 'name', 'img', 'description', 'fk_difficult', 'fk_category', 'steps', 'recipe_ingredient', 'fk_user']

    def create(self, validated_data): # Create method
        ingredients = validated_data.pop('recipe_ingredient') # In the view, we pass the recipeIngredients to the serializer.
        # The serializer can't handle the nested json for creation an update 
        


        recipe = Recipe.objects.create(**validated_data) # We create the recipe with the valid data object
  
        mainOne = False; 
        for i in ingredients:
            measurement = Measurement.objects.get(id=i['measurement']) 

            product = Product.objects.get(id=i['product'])

            if i['principal']:
                mainOne = True
            else:
                mainOne = False
            Ingredient.objects.create(main_ingredient=mainOne,
                                      amount=i['cantidad'],
                                      fk_measurement_unit_id=measurement.id,
                                      fk_product_id=product.id,
                                      fk_recipe_id=recipe.id)
            
    

        #
        #       recipe = Recipe.objects.create(**validated_data)
        #       #Ingredient.objects.create(fk_recipe=recipe, **ingredients)
        return recipe


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
    
        mainOne = False;
        for i in ingredients:
            measurement = Measurement.objects.get(id=i['measurement'])

            product = Product.objects.get(id=i['product'])

            if i['principal']:
                mainOne = True
            else:
                mainOne = False
            Ingredient.objects.create(main_ingredient=mainOne,
                                      amount=i['cantidad'],
                                      fk_measurement_unit_id=measurement.id,
                                      fk_product_id=product.id,
                                      fk_recipe_id=recipe.id )


    #
    #       recipe = Recipe.objects.create(**validated_data)
    #       #Ingredient.objects.create(fk_recipe=recipe, **ingredients)
        return recipe # Here we can return a HTTP Response or an objecto




class ReciepeImageSerialize(serializers.ModelSerializer): # this class was for test propouse
    class Meta:
        model = RecipeImage
        fields = ['image']
        
class RecipeSerializerJSON(serializers.ModelSerializer): # Return de value but with a nested json
    # Everything must be inside of the meta class
    #fk_difficult = DifficultySerializer(many=False) # Nested JSON serializer
    #fk_category = CategorySerializer(many=False) # Nested JSON serializer
    #recipe_ingredient = serializers.StringRelatedField(many=True) # __str__ nested serialize with other model that has a relationship with this one
    recipe_ingredient = IngredientSerializer(many=True, read_only=True) # the read only means that the field will not be modified
    #fk_difficult = serializers.StringRelatedField(many=False)  # __str__ nested serialize
    #fk_category = serializers.StringRelatedField(many=False)  # __str__ nested serialize

    # fk_user = serializers.StringRelatedField(many=False) # __str__ nested serialize

    class Meta:
        model = Recipe
        fields = ['id', 'slug', 'name', 'img', 'description', 'fk_difficult', 'fk_category', 'steps', 'recipe_ingredient', 'fk_user']

    def update(self, instance, validated_data):
        recipe_ingredientes = validated_data.pop('recipe_ingredient')
        
        recipe_ingredientes_instance = Ingredient.objects.filter(fk_recipe_id=instance.id)
        recipe_ingredientes_instance = list(recipe_ingredientes_instance)
        #img = validated_data.pop('img')
        

        Recipe.objects.filter(id=instance.id).update(**validated_data)

        # Poner mejor esta parte
        # instance.slug = validated_data.get('slug')
        # instance.name = validated_data.get('name')
        # instance.img = validated_data.get('img')
        # instance.description = validated_data.get('description')
        # instance.fk_difficult = validated_data.get('fk_difficult')
        # instance.fk_category = validated_data.get('fk_category')
        # instance.steps = validated_data.get('fk_category')

        for recipe_ing in recipe_ingredientes:
         
            measurement = Measurement.objects.get(id=recipe_ing['measurement'])
            product = Product.objects.get(id=recipe_ing['product'])
            if len(recipe_ingredientes_instance) > 0:
                ingredient = recipe_ingredientes_instance.pop(0)
               

                ingredient.fk_measurement_unit = measurement
                ingredient.fk_product = product
                ingredient.amount = recipe_ing['cantidad']
                ingredient.main_ingredient = recipe_ing['principal']
                ingredient.save()
            else:
                Ingredient.objects.create(main_ingredient=recipe_ing['principal'],
                                          amount=recipe_ing['cantidad'],
                                          fk_measurement_unit_id=measurement.id,
                                          fk_product_id=product.id,
                                          fk_recipe_id=instance.id)

        return HttpResponse({'message': 'Recipe Created'}, status=200)
