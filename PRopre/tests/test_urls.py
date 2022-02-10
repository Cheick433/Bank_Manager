from django .test import SimpleTestCase
from django.urls import reverse, resolve
from PRopre.views import ajouter_client, list_client, info_client, supprimer_client, modiffier_client, home

class TestUrls(SimpleTestCase):


    def test_ajouter_url_resolved(self):
        url = reverse('ajouter_client')
        print(resolve(url))
