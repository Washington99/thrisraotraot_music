from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length = 50)
    birth_name = models.CharField(max_length = 50, blank = True)
    monthly_listeners = models.IntegerField()
    bio = models.TextField(max_length = 700, blank = True)
    
    def __str__(self):
        return "{}".format(self.artist_name)

class Album(models.Model):
    album_name = models.CharField(max_length = 50)
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    description = models.CharField(max_length = 100)
    release_date = models.IntegerField()
    label = models.CharField(max_length = 50, blank = True)
    song_count = models.IntegerField(default = "0")
    
    def __str__(self):
        return "{}: {}".format(self.album_name, self.release_date)
    
class Song(models.Model):
    song_title = models.CharField(max_length = 50)
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    song_length = models.CharField(max_length = 10)
    music_video = models.BooleanField(default = False)
    lyrics = models.TextField(max_length = 10000, blank = True)
    
    def __str__(self):
        return "{} by {}".format(self.song_title, self.artist)
