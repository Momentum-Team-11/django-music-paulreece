# Generated by Django 4.0.3 on 2022-03-04 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_collection', '0002_album_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='favorite',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
