from django.contrib import admin
from locationModule import models
from rest_framework.authtoken.admin import TokenAdmin

#Modules
admin.site.register(models.City)
admin.site.register(models.Forecast)

#API token generator
TokenAdmin.raw_id_fields = ['user']