from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from horoscope_app.services import HoroscopeSource

hor_src = HoroscopeSource()


class ZodiacSignsView(TemplateView):
    """For main page"""
    template_name = "horoscope_app/index.html"

    def get(self, request: WSGIRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name,
                      {'zodiac_signs': hor_src.get_list_of_zodiac_signs()})


class HoroscopeView(TemplateView):
    """For horoscope of zodiac sign"""
    template_name = "horoscope_app/detail_horoscope.html"

    def get(self, request: WSGIRequest, zodiac_sign: str, *args, **kwargs) -> HttpResponse:
        if zodiac_sign == 'favicon.ico':
            return render(request, self.template_name)
        return render(request, self.template_name,
                      {'horoscope': hor_src.get_horoscope(zodiac_sign)})
