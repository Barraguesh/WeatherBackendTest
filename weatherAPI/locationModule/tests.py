from django.test import testcases, TestCase, Client
from django.urls import reverse, resolve
from django.core.management import call_command

from locationModule.views import index_view
from locationModule.models import City, Forecast

class TestUrls(testcases.SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('locationModule')
        self.assertEquals(resolve(url).func, index_view)

class TestViews(TestCase):
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('locationModule'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class TestModels(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            id=0000,
            name='City'
        )
        self.forecast = Forecast.objects.create(
            city=self.city,
            data='{"test": True}'
        )

    def test_city_model(self):
        self.assertEquals(self.city.name, 'City')

    def test_forecast_model(self):
        self.assertEquals(self.forecast.data, '{"test": True}')

class TestApiUpdate(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            id=8043,
            name='Vitoria-Gasteiz'
        )

    def test_index_view(self):
        args = []
        opts = {}
        call_command('updateWeather', *args, **opts)
