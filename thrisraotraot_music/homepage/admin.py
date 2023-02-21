from django.contrib import admin

# Register your models here.

from .models import Artist, Album, Song

class ArtistAdmin(admin.ModelAdmin):
    model = Artist

class AlbumAdmin(admin.ModelAdmin):
    model = Album
    
class SongAdmin(admin.ModelAdmin):
    model = Song
    
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
