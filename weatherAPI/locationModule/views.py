#Python/Django
import datetime
import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

#Models
from locationModule.models import City
from locationModule.models import Forecast

#Global variables
date_now = datetime.datetime.now()
date_db_format = "%Y-%m-%d"
date_pretty_format = "%Y-%m-%d %H:%M"

def index_view(request):
    args = {}
    #Example for scalability with more cities
    for city in City.objects.all():
        forecast = Forecast.objects.get(city=city)
        array_forecast = []
        json_data = forecast.data
        for x in range(1,7):
            array_forecast.append([json_data[f'day{x}']['date'], json_data[f'day{x}']['temperature_max'], json_data[f'day{x}']['temperature_min']])
        args['cities'] = {city.id: array_forecast}
    return render(request, 'index.html', args)