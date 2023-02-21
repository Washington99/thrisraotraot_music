from django.contrib import admin

# Register your models here.

from .models import Artist, Album, Song

class ArtistAdmin(admin.ModelAdmin):
    model = Artist
    
    list_display = ("artist_name", "birth_name", "monthly_listeners")
    
    search_fields = ("artist_name", "birth_name")
    
    list_filter = ("artist_name", "birth_name")

class AlbumAdmin(admin.ModelAdmin):
    model = Album
    
    list_display = ("album_name", "description", "release_date", "label", "song_count")
    
    search_fields = ("album_name", "description", "label")
    
    list_filter = ("album_name",)
    
class SongAdmin(admin.ModelAdmin):
    model = Song
    
    list_display = ("song_title", "song_length", "lyrics", "music_video")
    
    search_fields = ("song_title", "lyrics")
    
    list_filter = ("song_title",)
    
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
