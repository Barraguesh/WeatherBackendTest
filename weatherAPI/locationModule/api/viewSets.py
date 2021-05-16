#Python/Django
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

#Models
from locationModule.models import City
from locationModule.models import Forecast

#Serializers
from locationModule.api.serializers import CitySerializer
from locationModule.api.serializers import ForecastSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = all

class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    permission_classes = all