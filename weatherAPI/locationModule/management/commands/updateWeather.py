import requests
import json

from django.core.management.base import BaseCommand
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
            city = City.objects.get(id=city_id)
            Forecast.objects.get(city=city).delete()
            forecast = Forecast(city=city, data=json_data)
            forecast.save()
        else:
            print('Other response errors')