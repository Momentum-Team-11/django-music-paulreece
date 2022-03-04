"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music_collection import views as album_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', album_views.list_albums, name='list_albums'),
    path('albums/<int:pk>/', album_views.album_detail, name='album_detail'),
    path('artists/<int:pk>/', album_views.artist_detail, name='artist_detail'),
    path('artists/<int:pk>/album/', album_views.add_album, name='add_album'),
    path('artists/add', album_views.add_artist, name='add_artist'),
    path('albums/<int:pk>/edit/',
         album_views.edit_album,
         name='edit_album'),
    path('albums/<int:pk>/delete/',
         album_views.delete_album,
         name='delete_album'),
    path('albums/<int:pk>/favorite/',
         album_views.favorite_album,
         name='favorite_album'),
    path('albums/<int:pk>/remove_favorite/',
         album_views.remove_favorite,
         name='remove_favorite'),

]
