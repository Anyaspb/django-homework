# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from measurement.models import Sensor, Measure
from measurement.serializers import SensorsSerializer, SensorDetailSerializer, MeasureSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

class SensorDetailView(RetrieveAPIView, UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasureView(ListCreateAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer

