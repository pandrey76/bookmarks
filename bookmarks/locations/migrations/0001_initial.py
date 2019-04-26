# Generated by Django 2.0.13 on 2019-04-25 13:38

from django.db import migrations, models
import django.db.models.deletion


def create_bookmarks(apps, schema_editor):
    Bookmark = apps.get_model('locations', 'Bookmark')
    Comment = apps.get_model('locations', 'Comment')
    bookmark1 = Bookmark(link='google.com')
    bookmark1.save()
    bookmark2 = Bookmark(link='cnn.com')
    bookmark2.save()
    bookmark3 = Bookmark(link='apple.com')
    bookmark3.save()
    comment1 = Comment(text='These people make the iPhone', bookmark=bookmark3)
    comment1.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(db_index=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='locations.Bookmark')),
            ],
        ),
        migrations.RunPython(create_bookmarks)
    ]
