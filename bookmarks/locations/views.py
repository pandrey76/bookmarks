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


class SimpleHelloPerson(View):
    """
       View that returns Hello $person parameter
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>Hello {}</h1>'.format(request.GET['name']))


class SimpleHelloPersonVersion2(View):
    """
        View that return Hello $person parameter (version #2)
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>Hello {}</h1>'.format(kwargs['name']))


class TemplateHelloPerson(TemplateView):
    """
        View that uses template to return Hello $person parameter
    """
    template_name = 'locations/hello.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.kwargs['name']
        return context
