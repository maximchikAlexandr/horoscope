from django.urls import reverse
from django.test import TestCase

from horoscope_app.tests import ZODIACS, ZODIAC_FIXTURE


class ViewsTests(TestCase):
    fixtures = [ZODIAC_FIXTURE]

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_horoscope_pages(self):
        for latin_name, russian_name in ZODIACS:
            url = reverse('horoscope', kwargs={'zodiac_sign': latin_name})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
