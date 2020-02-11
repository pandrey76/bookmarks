from django.test import SimpleTestCase
from django.test.client import RequestFactory
from django.urls.base import reverse
from django.test import tag
from .views import TemplateHelloPerson


# from .models import Comment

# Create your tests here.

# Integration Test

class ITTest_TemplateHelloPerson(SimpleTestCase):

    # @tag('integration_test')
    # def test_render(self):
    #     response = self.client.get(
    #         reverse('hello-view4', kwargs={'name': 'Allan'}), follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.resolver_match.url_name, 'hello-view4')
    #     # print(response )
    #     self.assertContains(response, b'<title>Hello Allan</title>')
    #     self.assertContains(response, b'<p>There are 5 characters in your name</p>')
    #     self.assertContains(response, b'you have not won')


# Unit Testing

class UTTest_TemplateHelloPerson(SimpleTestCase):
    def setUp(self):
        super().setUp()
        self.request = RequestFactory().get('/fake-path')
        self.view = TemplateHelloPerson()
        self.setup_view_test(self.view, self.request)

    @tag('unit_test')
    def test_class_attributes(self):
        self.assertEqual(self.view.template_name, 'locations/hello.html')

    @tag('unit_test')
    def test_get_context_data(self):
        self.view.kwargs['name'] = 'Fred'
        context = self.view.get_context_data()
        self.assertEqual(context['name'], 'Fred')


def setup_view_test(view, request, *args, **kwargs):
    """
    Mimic as_view() returned callable, but returns view instance.

    args and kwargs are the same you would pass to ''reverse()''
    :param view:
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view

