## generic
from rest_framework import generics
##########

## Model
from ..models import Ingredient
########

## Serialize
from ..serialize import IngredientSerializer
############

class IngredienttList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
