from django.db import models
from django.db.models import Model
from django.db.models.fields import URLField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey
from django.db.utils import IntegrityError


# Create your models here.


class Bookmark(Model):
    """

    """

    link = URLField(max_length=1000, null=False, blank=False, db_index=True)

    def __str__(self):
        """

        :return:
        """
        return str(self.link)


class Comment(Model):
    """

    """

    bookmark = ForeignKey(Bookmark, on_delete=models.CASCADE, related_name='comments')
    time = DateTimeField(auto_now_add=True, null=False, blank=True)
    text = TextField()

    def __str__(self):
        """

        :return:
        """
        return self.text

    def link_str(self):
        return 'This comment: {} is for link: {}'.format(self.text, self.bookmark.link)
