## generic
from rest_framework import generics
##########

## Model
from ..models import Recipe
########

## Serialize
from ..serialize import RecipeSerializer
############

class RecipeList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # ADD the current user
    def perform_create(self, serializer):
        serializer.save(fk_user = self.request.user)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
