from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.


class SimpleHelloWord(View):
    """
        View that returns Hello World
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>Hello world</h1>')