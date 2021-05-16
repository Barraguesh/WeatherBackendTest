#Python/Django
from django.urls import include, path
from rest_framework import routers

from locationModule import views
from locationModule.api import viewSets

#API - Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'city', viewSets.CityViewSet)
router.register(r'forecast', viewSets.ForecastViewSet)

urlpatterns = [
    path('', views.index_view, name='locationModule'),

    path('api/', include(router.urls)),
]