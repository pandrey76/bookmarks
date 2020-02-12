from django.conf.urls import url, include
from django.urls import path
from . import views
from .views import SimpleHelloWord, SimpleHelloPerson, SimpleHelloPersonVersion2, TemplateHelloPerson,\
    SimpleHelloWorldAPI
from .views import BookmarkListView, BookmarkDetailView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('hello1/', SimpleHelloWord.as_view(), name='hello-view1'),
    path('hello2/', SimpleHelloPerson.as_view(), name='hello-view2'),
    path('hello3/<str:name>/', SimpleHelloPersonVersion2.as_view(), name='hello-view3'),
    path('hello4/<str:name>/', TemplateHelloPerson.as_view(), name='hello-view4'),
    path('hello_api/<str:name>/', SimpleHelloWorldAPI.as_view(), name='hello-api'),
]

standardview_urlpatters = [
    url(r'^bookmarks_trade_view/$', BookmarkListView.as_view()),
    url(r'^bookmarks_trade_view/(?P<pk>[0-9]+)/$', BookmarkDetailView.as_view())
]

standardview_urlpatters = format_suffix_patterns(standardview_urlpatters)

urlpatterns += standardview_urlpatters
