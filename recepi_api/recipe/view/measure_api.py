## generic
from rest_framework import generics
##########

## Model
from ..models import Measurement
########

## Serialize
from ..serialize import MeasurementSerializer
############

class MeasurementList(generics.ListCreateAPIView):
    # The most generic you can be
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
