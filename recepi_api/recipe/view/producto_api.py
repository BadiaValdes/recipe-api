## generic
from rest_framework import generics
##########

## Model
from ..models import Product
########

## Serialize
from ..serialize import ProductSerializer
############

class ProductList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
