## generic
from rest_framework import generics
##########

## Model
from ..models import Difficulty
########

## Serialize
from ..serialize import DifficultySerializer
############

class DifficultyList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer

class DifficultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
