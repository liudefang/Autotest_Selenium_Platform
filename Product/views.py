from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from Product.models import Browser


class Public:
    @staticmethod
    def data(request):
        browsers = Browser.objects.all()
        browsers_re = list()
        for browser in browsers:
            dic = model_to_dict(browsers,)