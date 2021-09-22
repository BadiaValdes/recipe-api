## generic
from rest_framework import generics, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
##########

## render
from rest_framework import renderers
#########

## Response
from rest_framework.response import Response
###########

## Model
from ..models import Recipe,Difficulty,Category,Product,Ingredient
from user.models import User
########

## Decorators
from rest_framework.decorators import api_view
#############

from django.http import HttpResponse

## Serialize
from ..serialize import RecipeSerializer, RecipeSerializerCreate, ReciepeImageSerialize, RecipeSerializerJSON
############

## Permissions
from rest_framework import permissions, filters
from ..permissions import IsOwnerOrReadOnly

## QUery
from django.db.models import Q, Count

##############

import json

# Don't repeat yourself
class RecipeObject (object):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeList(RecipeObject, generics.ListCreateAPIView):
    # The most generic you can be
   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
    IsOwnerOrReadOnly
    ]   
     
    filter_backends = [filters.SearchFilter] # Default rest filters
    search_fields = ['fk_user__id'] # lookup fields


    def perform_create(self, serializer):
        ri = json.loads(self.request.POST['recipe_ingredient'])
        cat = Category.objects.get(id=self.request.POST['fk_category'])
        dif = Difficulty.objects.get(id=self.request.POST['fk_difficult'])
        serializer.save(recipe_ingredient=ri, fk_category=cat, fk_difficult=dif)
        
    # Value depending on the parameter 
    # with the filters, this part is unnecesary
    def get_queryset(self):
    	
    	# Ask if the kwargs exist and then return the recipe filtered
    	if len(self.kwargs) > 0 and self.kwargs['userid']:
    		return Recipe.objects.filter(fk_user=self.kwargs['userid'])
    		
    	else:
    		return Recipe.objects.all()
    		
    	
    


    # ADD the current user
    # def perform_create(self, serializer):
    #     print("pase por aqui")
    #     serializer.save(fk_user = self.request.user)

class RecipeCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializerCreate
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer, *args, **kwargs):
        ri = json.loads(self.request.POST['recipe_ingredient'])
        serializer.save(recipe_ingredient=ri)
        #serializer.save(fk_user=self.request.user)



    # def post(self, request, *args, **kwargs):
    #     print(request.body)
    #     file_serialize = RecipeSerializerCreate(data=request.data)
    #
    #     if file_serialize.is_valid():
    #         file_serialize.save()
    #         return HttpResponse({'message': 'Recipe Created'}, status=200)
    #     else:
    #         return HttpResponse({'message': 'BADD'}, status=400)
    # #     dataDic = json.loads(request.body)
    # #     print(dataDic['img'])
    # #     recipe_name = dataDic['name']
    # #     slug = dataDic["slug"]
    # #     img = dataDic["img"]
    # #     description = dataDic["description"]
    # #     fk_difficult = dataDic["fk_difficult"]
    # #     fk_category = dataDic["fk_category"]
    # #     steps = dataDic["steps"]
    # #     recipe_ingredient = dataDic["recipe_ingredient"]
    # #     fk_user = dataDic["fk_user"]
    # #
    # #     print("aqui")
    # #
    # #     dificlut = Difficulty.objects.get(id=fk_difficult)
    # #     category = Category.objects.get(id=fk_category)
    # #     user = User.objects.get(id=fk_user)
    # #
    # #
    # # #
    # #     Recipe.objects.create(name=recipe_name, slug=slug, img=img, description=description, fk_difficult=dificlut, fk_category=category, steps=steps, fk_user=user)
    # # #     for recip in recipe_ingredient:
    # # #         print(recip)
    #     return HttpResponse({'message': 'Recipe Created'}, status=200)


class RecipeUploadImage(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = ReciepeImageSerialize(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # for search propuse
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly
                          ]
    def perform_destroy(self, instance):
        instance.img.delete(save=True)
        instance.delete()
        
        
      
                          
class RecipeDetailJSON(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializerJSON
    # for search propuse
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly
                          ]

    def perform_update(self, serializer):
        ri = json.loads(self.request.POST['recipe_ingredient'])
        #id = self.kwargs.get('pk')

        serializer.save(recipe_ingredient=ri)
        # serializer.save(fk_user=self.request.user)


# HTML REPRESENTATION of the model
class RecipeHig(generics.GenericAPIView):
    renderer_classes = [renderers.StaticHTMLRenderer]
    queryset = Recipe.objects.all()

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response([snippet.name, "---", snippet.description])

@api_view(['GET', 'POST'])
def searchFor(request, *args, **kwargs):
    if request.method == 'GET':
        ingredients = json.loads(request.GET['ingredients']) # Get ingredients ARRAY
        difficult_temp = request.GET['difficul'];	
        slide_value = request.GET['slideValue'];    
        product = Product.objects.get(id=ingredients.pop(0)['product']['id'])  # Get first Ingredients (MAIN)
        ingredients_length = len(ingredients)
	
        if difficult_temp != '0':
            
            difficult = Difficulty.objects.get(id=difficult_temp) # Get Difficult
            print(difficult)
            recipe = Recipe.objects.filter(
                Q(recipe_ingredient__fk_product__id=product.id) & Q(recipe_ingredient__main_ingredient=True) & Q(
                    fk_difficult=difficult))
        else:
            recipe = Recipe.objects.filter(
                Q(recipe_ingredient__fk_product__id=product.id) & Q(recipe_ingredient__main_ingredient=True))


        if len(ingredients) > 0 and int(slide_value) != 0:
            if int(slide_value) == 100: 
                recipe = allTheIngredientsMatters(ingredients,recipe)
            else:
                recipe = onlyTheMainIngredientsMatters(ingredients,recipe)
            if int(slide_value) == 50:
            	recipe = theAmountOfIngredientGreaterThan(int(ingredients_length*0.5),recipe)
            elif int(slide_value) == 75:
               recipe = theAmountOfIngredientGreaterThan(int(ingredients_length*0.75),recipe)
        
        serealizaer_result = RecipeSerializer(recipe, many=True)
        return Response(serealizaer_result.data, status=status.HTTP_200_OK, content_type='application/json')


def allTheIngredientsMatters(rest_of_ingredients, filter_model_instance):
    for rest in rest_of_ingredients:
        product = Product.objects.get(id=rest['product']['id'])
        filter_model_instance = filter_model_instance.filter(Q(recipe_ingredient__fk_product__id=product.id)).distinct()
    return filter_model_instance

def onlyTheMainIngredientsMatters(rest_of_ingredients, filter_model_instance):
    z = []
    for rest in rest_of_ingredients:
        product = Product.objects.get(id=rest['product']['id'])
        z.append(product.id)
    filter_temp = filter_model_instance.filter(Q(recipe_ingredient__fk_product__id__in=z)).distinct()
    # if the filter process is empty,
    if len(filter_temp) > 0:
        filter_model_instance = filter_temp
    return filter_model_instance

def theAmountOfIngredientGreaterThan(greaterThan, filter_model_instance):
    return filter_model_instance.annotate(c = Count('recipe_ingredient__fk_product__id')).filter(c__gt = greaterThan)

    # Contains all the products
    # for rest in rest_of_ingredients:
    #     product = Product.objects.get(id=rest['product'])
    #     z.append(product.id)
    #     print(z)
    #     # Exact and in the same order
    #     filter_model_instance = filter_model_instance.filter(Q(recipe_ingredient__fk_product__id__contains=product.id))

    # Simple filter, Can be use as a conditional, gets all the recipe that contains any of those ingredients
    #.filter(Q(recipe_ingredient__fk_product__id__in=z))

    # All the results must to be different
    #.distinct()

    # Greater than 1 ingredient
    #.annotate(c = Count('recipe_ingredient__fk_product__id')).filter(c__gt = 1)

    # All the ingredients in the recipe
    #.filter(Q(recipe_ingredient__fk_product__id__contains=product.id))
