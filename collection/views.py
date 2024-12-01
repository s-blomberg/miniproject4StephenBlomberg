from .models import Album
from .forms import AlbumForm, CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

#URL logic/functions/glue

def homepage(request):
    # Example: Show latest albums
    latest_albums = Album.objects.order_by('-id')[:5]
    return render(request, 'collection/homepage.html', {'latest_albums': latest_albums})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'collection/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'collection/album_detail.html', {'album': album})


@login_required
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'collection/album_form.html', {'form': form})


@login_required
def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', pk=pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'collection/album_form.html', {'form': form})

@login_required
def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'collection/album_confirm_delete.html', {'album': album})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})