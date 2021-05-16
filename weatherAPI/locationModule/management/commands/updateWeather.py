import requests
import json

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist 

from locationModule.models import City, Forecast

class Command(BaseCommand):
    help = 'Updates the DB with results provided by TuTiempo API'

    def handle(self, *args, **options):
        city_id = '8043'
        api_key = '45Yqa4a4qqXvs5S'
        url = f'https://api.tutiempo.net/json/?lan=es&apid={api_key}&lid={city_id}'
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            try:
                city = City.objects.get(id=city_id)
            except ObjectDoesNotExist:
                #Hardcoded because of the nature of this project
                City(id=city_id, name='Vitoria-Gasteiz').save()
                city = City.objects.get(id=city_id)
            try:
                Forecast.objects.get(city=city).delete()
            except ObjectDoesNotExist:
                print('Warning: Forecast not in the database, adding it.')
            forecast = Forecast(city=city, data=json_data)
            forecast.save()
        else:
            print('Other response errors')