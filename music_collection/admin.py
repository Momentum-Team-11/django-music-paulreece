from django.contrib import admin
from .models import Album
from .models import Artist

admin.site.register(Album)
admin.site.register(Artist)
