from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Bookmark, Comment, Note, Like
from .serializers import BookmarkSerializer


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


class SimpleHelloWorldAPI(View):
    """
    View that returns a name parameter in a JSON response
    """

    def get(self, request, *args, **kwargs):
        if kwargs['name'].lower() != 'fred':
            return JsonResponse(
                {
                    'description': 'This endpoint welcomes the user',
                    'welcome': 'Hello {}'.format(kwargs['name'])
                },
                status=200
            )
        else:
            return JsonResponse(
                {
                    'description': 'This demonstrates an error',
                    'error': '{} is not an authorised user'.format(
                        kwargs['name']
                    )
                },
                status=403
            )


class BookmarkListView(APIView):
    """
    List all bookmarks, or create a new bookmark
    """

    def get(self, request, format=None):
        bookmarks = Bookmark.objects.all()
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookmarkDetailView(APIView):
    """
    Retrive, update or delete a bookmark.
    """

    def get_object(self, pk):
        try:
            return Bookmark.objects.get(pk=pk)
        except Bookmark.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bookmark = self.get_object(pk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bookmark = self.get_object(pk)
        serializer = BookmarkSerializer(bookmark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bookmark = self.get_object(pk)
        bookmark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)