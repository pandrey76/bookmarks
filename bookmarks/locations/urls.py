from django.conf.urls import url, include
from django.urls import path
from locations import views
from .views import SimpleHelloWord, SimpleHelloPerson

urlpatterns = [
    path('hello1/', SimpleHelloWord.as_view(), name='hello-view1'),
    path('hello2/', SimpleHelloPerson.as_view(), name='hello-view2'),
]
