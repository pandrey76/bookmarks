from django.conf.urls import url, include
from django.urls import path
from locations import views
from .views import SimpleHelloWord, SimpleHelloPerson, SimpleHelloPersonVersion2

urlpatterns = [
    path('hello1/', SimpleHelloWord.as_view(), name='hello-view1'),
    path('hello2/', SimpleHelloPerson.as_view(), name='hello-view2'),
    path('hello3/<str:name>/', SimpleHelloPersonVersion2.as_view(), name='hello-view3'),
]
