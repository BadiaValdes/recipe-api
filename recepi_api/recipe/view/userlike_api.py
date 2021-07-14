## generic
from rest_framework import generics
##########

## Model
from ..models import UserLike
########

## Serialize
from ..serialize import UserLikeSerializer
############

class UserLikeList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = UserLike.objects.all()
    serializer_class = UserLikeSerializer

class UserLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserLike.objects.all()
    serializer_class = UserLikeSerializer
