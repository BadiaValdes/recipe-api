## generic
from rest_framework import generics, viewsets
##########

## render
from rest_framework import renderers
#########

## Response
from rest_framework.response import Response
###########

## Model
from ..models import Recipe,Difficulty,Category
########

from django.http import HttpResponse

## Serialize
from ..serialize import RecipeSerializer, RecipeSerializerCreate
############

## Permissions
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly

##############

class RecipeList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # ADD the current user
    def perform_create(self, serializer):
        print("pase por aqui")
        serializer.save(fk_user = self.request.user)

class RecipeCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializerCreate

    def perform_create(self, serializer, *args,**kwargs):
        print(serializer)
        print("pase por aqui")
        serializer.save(fk_user=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     recipe_name = request.data["name"]
    #     slug= request.data["slug"]
    #     img = request.data["img"]
    #     description = request.data["description"]
    #     fk_difficult = request.data["fk_difficult"]
    #     fk_category = request.data["fk_category"]
    #     steps = request.data["setps"]
    #     recipe_ingredient = request.data["recipe_ingredient"]
    #     fk_user = self.request.user
    #
    #     print("aqui")
    #
    #     dificlut = Difficulty.objects.get(id=fk_difficult)
    #     category = Category.objects.get(id=fk_category)
    #
    #     recipe = Recipe.objects.create(name=recipe_name, slug=slug, img=img, description=description, fk_difficult=dificlut, fk_category=category, steps=steps, fk_user=fk_user)
    #     for recip in recipe_ingredient:
    #         print(recip)
    #     return HttpResponse({'message': 'Recipe Created'}, status=200)



class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          #IsOwnerOrReadOnly
                          ]


# HTML REPRESENTATION of the model
class RecipeHig(generics.GenericAPIView):
    renderer_classes = [renderers.StaticHTMLRenderer]
    queryset = Recipe.objects.all()

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response([snippet.name, "---", snippet.description])
