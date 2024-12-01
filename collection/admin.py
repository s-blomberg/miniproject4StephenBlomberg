from django.contrib import admin
from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'variant', 'release_date', 'description', 'cover_image')
    search_fields = ('title', 'artist')
