from django.shortcuts import render
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm
from django.shortcuts import render, redirect, get_object_or_404


def list_albums(request):
    albums = Album.objects.all()
    artists = Artist.objects.all()
    return render(request, "album_list.html",
                  {"albums": albums, "artists": artists})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "album_detail.html",
                  {"album": album})


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    albums = Album.objects.all()
    return render(request, "artist_detail.html",
                  {"artist": artist, "albums": albums})


def add_artist(request):
    if request.method == 'GET':
        form = ArtistForm()
    else:
        form = ArtistForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "add_artist.html", {"form": form})


def add_album(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.the_artist = artist
            album.save()
            return redirect(to='list_albums')

    return render(request, "add_album.html", {"form": form, "artist": artist})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "edit_album.html", {
        "form": form,
        "album": album
    })


def favorite_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        favorite = Album
    else:
        favorite = Album(request.method == 'POST')
        Album.objects.filter(pk=album.pk).update(favorite="⭐")
        return redirect(to='list_albums')
    return render(request, 'favorite_album.html', {
        "album": album,
        "favorite": favorite
    })


def remove_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        favorite = Album
    else:
        favorite = Album(request.method == 'POST')
        Album.objects.filter(pk=album.pk).update(favorite="")
        return redirect(to='list_albums')
    return render(request, 'remove_favorite.html', {
        "album": album,
        "favorite": favorite
    })


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, 'delete_album.html',
                  {"album": album})
