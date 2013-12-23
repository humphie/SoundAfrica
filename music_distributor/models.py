from django.db import models
from django.contrib.auth.models import User
from music_publisher.models import Album
from music_publisher.models import Song
from music_publisher.models import DownloadRating
"""

THIS MODEL IS UNIQUE TO THE CUSTOMER BUT  , IT BORROWS DATA FROM THE MODEL OF THE MUSICIAN SO AS TO GAIN ACCESS TO
GIVEN PROPERTIES OF THE ALBUMS, SONGS AND PERHAPS OTHER RELATED DATA ...

"""

# The customers profile information
class Customer(models.Model):
    user = models.ForeignKey(User)
    brief_desc = models.CharField(max_length=300, null=True)
    contact = models.IntegerField()
    veri_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to="/media/profile_pictures", null=True)


# This holds the credit that the customer has
class Credit(models.Model):
    customer = models.ForeignKey(Customer)
    current = models.IntegerField()


# This keeps a record of all the previous purchases made by the customer
class Purchases(models.Model):
    purchase_holder = models.ForeignKey(Customer)
    previous_purchased_albums = models.ForeignKey(Album)
    download_rating = models.ForeignKey(DownloadRating)
    previous_purchased_songs = models.ForeignKey(Song)
    purchase_price = models.IntegerField()
    purchase_date = models.DateTimeField()


# This will be used to keep track of archives that may have not finished their download
class Downloads(models.Model):
    archive_path = models.FilePathField()
    status = models.NullBooleanField()
    customer = models.ForeignKey(Customer)













