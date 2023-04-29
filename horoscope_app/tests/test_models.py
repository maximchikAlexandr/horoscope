from django.test import TestCase

from horoscope_app.models import Zodiac
from horoscope_app.tests import ZODIACS, ZODIAC_FIXTURE


class ZodiacTest(TestCase):
    fixtures = [ZODIAC_FIXTURE]

    def test_query_of_zodiac(self):
        for latin_name, russian_name in ZODIACS:
            zodiac = Zodiac.objects.get(latin_name=latin_name)
            self.assertEquals(zodiac.russian_name, russian_name)
