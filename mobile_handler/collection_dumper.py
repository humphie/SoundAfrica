__author__ = 'william'

from protobuffers import DataBuffer_pb2
from theWave.models import Album
from theWave.models import Song
import base64
class Collection_handler:
# THIS FILE WILL SIMPLY PACK AND ENTIRE COLLECTION INTO A PROTOBUFFER

    def __init__(self):
        """
        CREATE THE INITIAL OBJECTS OF INTEREST THAT WILL BE DEALT WITH IN THIS POINT:

        """
        self.__collection = None
        self.__album_queryset = None
        self.__song_queryset = None
        self.__songs = list()
        self.__collection = DataBuffer_pb2.Collection()
    def send_collection(self):
        self.__album_queryset = Album.objects.all() # GET ALL THE DATA AS A QUERY SET
        for album_iter in self.__album_queryset:
            self.__song_queryset = Song.filter(album=album_iter)
            song_set = self.song_packer(self.__song_queryset,album_iter.year,album_iter.name)
            packed_album = self.__album_packer(self.__album_queryset,song_set)
            self.__collection.albums.add(packed_album) # Dumping to create a collection


        return self.__collection


# THIS WILL PACK
    def song_packer(self,song,year,album_name):


            song_pb = DataBuffer_pb2.Song()
            song_pb.trackNumber = song.track_number
            song_pb.title = song.title
            song_pb.genre = song.genre
            song_pb.artist = song.artist
            song_pb.year = year
            song_pb.path = song.audio_file
            song_pb.comment = song.comment
            song_pb.description = song.description
            song_pb.language = song.language
            song_pb.album = album_name

            return song_pb

    def album_packer(self,album_desriptor,songs):

        with open(album_desriptor.cover_pic,"rb") as imageFile:

            album_pb = DataBuffer_pb2.Album()
            album_pb.albumName = album_desriptor.name
            album_pb.albumArtist = album_desriptor.albumArtist
            for song in songs:
                  album_pb.song.add(song)
            album_pb.coverArt = base64.b64encode(imageFile.read())
            album_pb.price = album_desriptor.price
            album_pb.rating = 0

        return album_pb


