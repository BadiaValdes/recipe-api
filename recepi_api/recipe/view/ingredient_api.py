## generic
from rest_framework import generics
##########

## Model
from ..models import Ingredient
########

## Serialize
from ..serialize import IngredientSerializer
############

## Permissions
from rest_framework import permissions


##############


class IngredienttList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
   #e permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
