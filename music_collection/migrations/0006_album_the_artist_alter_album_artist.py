# Generated by Django 4.0.3 on 2022-03-04 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_collection', '0005_remove_album_the_artist_alter_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='the_artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='music_collection.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=200),
        ),
    ]
