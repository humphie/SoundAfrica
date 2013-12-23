from sound_frica import settings

__author__ = 'william'

# THIS MODULE IS SIMPLY FOR HANDLING THE ORDERS AND ALSO THE ALGORITHM FOR BATCHING DATA

from music_distributor.models import Album
from music_distributor.models import Song
from music_distributor.models import CreditAccount
from protobuffers.Order_pb2 import Order as order_proto
import tarfile

class Order_Handler:
    def __init__(self):
        self.__album = None
        self.__songs = list()

        self.__album_pb2 = Album()
        self.__song = None
        self.__order = None
        self.__song_queryset = None
        self.__archive_name = None
        self.__temp_folder = "/upload_dir/-----[You put a path here]"
        self.__username = None
        self.__passowrd = None
        self.__credit = 0
        self.__user
    def search_album(self):

        album = Album.objects.filter(name = self.__order.album_name)
        self.__song_queryset = Song.objects.filter(album = album)


    def process_order(self, order_string):
        self.__order = order_proto.ParseFromString(order_string)
        self.search_album()
        self.file_archiving_utility()

    def file_archiving_utility(self):


        # GET THE SONGS IN THE QUERY SET AND START PACKING THEM.
        # RETURN THE PATH TO THE ARCHIVE
        self.__archive_name = self.__album.name+".tar.gz"
        tar = tarfile.open(self.__archive_name, "w:gz")
        if len(self.__song_queryset) > 1:
            for song in self.__song_queryset:

                tar.add(self.__temp_folder, song.audio_file)
            tar.close()

        return self.__album.name+".tar.gz"


    def send_processed_order(self):
        # First Punch in the credit status
        self.check_users_credit()

        # CREATE A HYPER-LINK TO BE SENT IN THE ORDER
        self.__order.archivePath = "http://www.soundafrica.com/media/download_holder/"+self.file_archiving_utility()
        return self.__order

    #def check_current_credit(self):

        # CHECK THE CURRENT BALANCE OF THE USER

    #def proceed_with_delete(self):

    def check_users_credit(self):
        # We will simply get the order and extract/instill credit details

        self.__credit = CreditAccount.objects.filter(user = self.__user)
        return self.__credit
        self.__order.credit = self.__credit