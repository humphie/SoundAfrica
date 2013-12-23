__author__ = 'william'

from music_publisher.models import Album
from music_publisher.models import DownloadRating
# THIS CLASS WILL CONTAIN ALGORITHMS TO SMARTLY SEARCH THE DATABASE FOR REQUIRED RESULTS

# QUEST -> HIGHEST DOWNLOADED
# MOST POPULAR ->
# NEWEST RELEASES
# UP-COMING
# FREE -ALBUMS
# SINGLES
# GROUPS
# COLLABORATIONS

class Algorithm:
    def __init__(self):
        self.__result_new_releases = None
        self.__result_most_popular = None
        self.__result_most_downloaded = None



    def aquire_highest_downloaded(self):

        self.__result_most_downloaded = Album.objects.all().orderby('-album_rating') # THE HIGHEST DOWNLOADS, THEN

    def aquire_most_popular_album(self):
        self.__result_most_popular = DownloadRating.objects.filter().orderby('-album_download_number') # THE HIGHEST STARS , THE ARRANGE THEM IN ORDER

    def aquire_new_releases(self):

        self.__result_new_releases = Album.objects.filter().orderby() # THE YEAR , THE FROM NEWEST IN 2 WEEKS/ 3 WEEKS

    # Chunk Sizing algorithms


    # sorting list sets for data

    #




