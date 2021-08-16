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
from ..models import Recipe,Difficulty,Category
from user.models import User
########

from django.http import HttpResponse

## Serialize
from ..serialize import RecipeSerializer, RecipeSerializerCreate, ReciepeImageSerialize, RecipeSerializerJSON
############

## Permissions
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly

##############

import json

class RecipeList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
    IsOwnerOrReadOnly
    ]


    def perform_create(self, serializer):
        ri = json.loads(self.request.POST['recipe_ingredient'])
        cat = Category.objects.get(id=self.request.POST['fk_category'])
        dif = Difficulty.objects.get(id=self.request.POST['fk_difficult'])
        serializer.save(recipe_ingredient=ri, fk_category=cat, fk_difficult=dif)


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
