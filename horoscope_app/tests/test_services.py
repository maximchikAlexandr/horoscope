from django.test import TestCase
from django.db.models.query import QuerySet

from horoscope_app.services import HoroscopeSource
from horoscope_app.tests import ZODIACS, ZODIAC_FIXTURE


class HoroscopeSourceTest(TestCase):
    fixtures = [ZODIAC_FIXTURE]

    @staticmethod
    def test_get_list_of_zodiac_signs():
        list_of_zodiac_signs = HoroscopeSource.get_list_of_zodiac_signs()
        assert isinstance(list_of_zodiac_signs, QuerySet)
        assert len(list_of_zodiac_signs) == len(ZODIACS)

    @staticmethod
    def test_get_horoscope():
        horoscope_srs = HoroscopeSource()
        for latin_name, russian_name in ZODIACS:
            horoscope = horoscope_srs.get_horoscope(latin_name)
            assert isinstance(horoscope, dict)
            assert "russian_name" in horoscope.keys()
            assert horoscope["russian_name"] == russian_name
            assert "horoscope" in horoscope.keys()
            assert isinstance(horoscope["horoscope"], dict)

    @staticmethod
    def test_is_actual_horoscope():
        horoscope_srs = HoroscopeSource()
        flag = horoscope_srs._HoroscopeSource__is_actual_horoscope()
        assert isinstance(flag, bool)
