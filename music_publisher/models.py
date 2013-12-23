from django.db import models
from audiofield.fields import AudioField
from django.contrib.auth.models import User




# Create your models here.
class Musician(models.Model):
    user = models.ForeignKey(User)
    brief_desc = models.CharField(max_length=300, null=True)
    contact = models.IntegerField()
    veri_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to="/media/profile_pictures", null=True)


class Album(models.Model):
        artist = models.ForeignKey(Musician)
        name = models.CharField(max_length=20)
        description = models.CharField(max_length=500)
        language = models.CharField(max_length=40)
        year = models.DateField()
        flag = models.CharField(max_length=40)
        price = models.IntegerField(null=True)
        cover_pic = models.ImageField(upload_to="/media/cover_art", null=True)
        album_rating = models.IntegerField()

class Song(models.Model):
    audio_file = AudioField(upload_to='/media/uploads', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))
    track_number = models.CharField(max_length=50, blank=True)
    comment      = models.CharField(max_length=50,blank=True)
    title        = models.CharField(max_length=50, blank=True)
    description  = models.CharField(max_length=50,blank=True)
    language     = models.CharField(max_length=50,blank=True)
    artist       = models.CharField(max_length=50, blank=True)
    album        = models.ForeignKey(Album)
    genre        = models.CharField(max_length=50,blank=True)
    song_rating = models.IntegerField()

class DownloadRating(models.Model):

    album_title = models.CharField(max_length=50, blank = True)
    album_rating = models.IntegerField()
    album_download_number = models.IntegerField()









