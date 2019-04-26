from django.conf.urls import url, include
from django.urls import path
from locations import views
from .views import SimpleHelloWord

urlpatterns = [
    path('hello1/', SimpleHelloWord.as_view(), name='hello-view1'),
]
