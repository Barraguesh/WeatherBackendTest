from django.db import models

class City(models.Model):
    id = models.CharField(
        max_length=1000,
        verbose_name='ID',
        primary_key=True
    )
    name = models.CharField(
        max_length=1000,
        verbose_name='Name'
    )
    
    def __str__(self):
        return str(self.name)

class Forecast(models.Model):
    city = models.ForeignKey(
        'City',
        on_delete=models.PROTECT,
        verbose_name='City'
    )
    data = models.JSONField()

    def __str__(self):
        return str(self.city)