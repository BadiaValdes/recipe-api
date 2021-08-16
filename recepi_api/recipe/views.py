from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Default api call
@api_view(['GET']) # this will be the main view of the API, here we can see the links of every model created in the database
def api_root(request, format=None):
    return Response({
        'category': reverse('category', request=request, format=format),
        'difficulty': reverse('difficulty', request=request, format=format),
        'measurement': reverse('measurement', request=request, format=format),
        'product': reverse('product', request=request, format=format),
        'recipe': reverse('recipe', request=request, format=format),
        'userLike': reverse('userLike', request=request, format=format),
        'ingredient': reverse('ingredient', request=request, format=format),
        'user': reverse('user', request=request, format=format),

    })
