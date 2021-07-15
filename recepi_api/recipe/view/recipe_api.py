## generic
from rest_framework import generics
##########

## render
from rest_framework import renderers
#########

## Response
from rest_framework.response import Response
###########

## Model
from ..models import Recipe
########

## Serialize
from ..serialize import RecipeSerializer
############

## Permissions
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly

##############

class RecipeList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # ADD the current user
    def perform_create(self, serializer):
        serializer.save(fk_user = self.request.user)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# HTML REPRESENTATION of the model
class RecipeHig(generics.GenericAPIView):
    renderer_classes = [renderers.StaticHTMLRenderer]
    queryset = Recipe.objects.all()

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response([snippet.name, "---" ,snippet.description])
