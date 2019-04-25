from django.test import SimpleTestCase
from .models import Comment

# Create your tests here.


class TestComment(SimpleTestCase):
    """

    """

    def test_str(self):
        """

        :return:
        """
        comment = Comment(text='my test string')
        self.assertEqual(str(comment), 'my test string')
