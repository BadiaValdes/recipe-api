from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..models import Category
from ..serialize import CategorySerializer

from django.http import Http404

## Decorators
from rest_framework.decorators import api_view, APIView
#############

## Response
from rest_framework.response import Response
###########

## Status
from rest_framework import status
#########

## MIX
from rest_framework import generics, mixins
######

## Permissions
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
######


# Create your views here.

# don't use @csrf_exempt, the only purpose of it is for example
# @api_view(['GET', 'POST']) # Allowed methods
# def category_list(request, format=None):
#     # the format=None specify the incoming url format example http://example.com/api/items/4.json.
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Category.objects.all()
#         serializer = CategorySerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         var = "Hola"
#         data.slug = data.name.lower().replace(" ", "-")
#         serializer = CategorySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def category_details(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CategorySerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = CategorySerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Class base view

class CategoryCommon(object):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryList(CategoryCommon, generics.ListCreateAPIView):
    # The most generic you can be
    pass

class CategoryCreate(CategoryCommon, generics.CreateAPIView):
    pass

    # mixin and generic api view (mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView)
    # Use this to left the logic to the frontend
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    #
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     #request.data['slug'] = name_to_lowr_case(request.data['name'])
    #     print(request.data['slug'])
    #     return self.create(request, *args, **kwargs)

    # with APIView
    # def get(self, request, format=None):
    #     snippets = Category.objects.all()
    #     serializer = CategorySerializer(snippets, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     # Modify the slug
    #     request.data['slug'] = name_to_lowr_case(request.data['name'])
    #     # print(request.data['slug'])
    #     # End Modification
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetails(CategoryCommon, generics.RetrieveUpdateDestroyAPIView):
    pass

    # with mixins and generic api view (mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView)
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    #
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

    # with APIView
    # def get_object(self, pk):
    #     try:
    #         return Category.objects.get(pk=pk)
    #     except Category.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = CategorySerializer(snippet)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     request.data['slug'] = name_to_lowr_case(request.data['name'])
    #     serializer = CategorySerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

def name_to_lowr_case(variable):
    return variable.lower().replace(" ", "-")
