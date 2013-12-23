__author__ = 'william'

# THIS CLASS WILL ALLOW META DATA ADDITION , FILE DELETION AND ALBUM
# APPENDING SO THAT THE MODEL IS NOT TOO CLOSE TO THE VIEW AND CODE
# CAN BE EASILY CHANGED WITHOUT FUSSING ABOUT IT

from mutagen.easyid3 import EasyID3
from django.utils.translation import ugettext_lazy as
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from mutagen.id3 import ID3, TRCK, TIT2, TPE1, TALB, TDRC, TCON, COMM, APIC


class AlbumEditor:
    def __init__(self):


    def song_tagger(self):


class SongEditor:
    def __init__(self):

        self.__track_number = None
        self.__title = None
        self.__genre = None
        self.__file = None
        self.__artist = None
        self.__year = None
        self.__cover_art = None
        self.__comment = None
        self.__description = None
        self.__language = None
        self.__album = None

class MP3_Tagger:
    def __init__(self,track_number,title,artist,album,year,genre,language,description,cover_art,comment):
        self.__track_number = track_number
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__year = year
        self.__genre = genre
        self.__language = language
        self.__description
        self.__comment = comment
        self.__cover_art = cover_art

    def create_tag(self,audio_file):
        audio = ID3() # CREATING ID3 OBJECT FOR TAGGING
        # BELOW IS THE TAGGING FACILITY OF THE PROGRAM
        audio.add(TRCK(encoding = 3,text = u(self.__track_number))
        audio.add(TIT2(encoding = 3,text = u(self.__title)))
        audio.add(TPE1(encoding = 3,text = u(self.__artist)))
        audio.add(TALB(encoding = 3,text = u(self.__album)))
        audio.add(TDRC(encoding = 3,text = u(self.__year)))
        audio.add(TCON(encoding = 3,text = u(self.__genre)))
        audio.add(COMM(encoding = 3,text = u(self.__language,self.__description,self.__comment)))
        audio.add(APIC(3,u'image/jpg',3,u'FrontCover',open(self.__cover_art).read()))

        # SAVE THE TAG TO THE FILE
        audio.save(audio_file)





    def add_metainfo(self,track_number,title,artist,album,year,genre,language,description,cover_art,comment,file):
         self.set_track_number(track_number)
         self.set_title(title)
         self.set_album(album)
         self.set_artist(artist)
         self.set_genre(genre)
         self.set_language(language)
         self.set_description(description)
         self.set_year(year)
         self.set_cover_art(cover_art)
         self.set_comment(comment)
         self.set_file(file)




    def save_metainfo(self):
         mp3_tag = self.MP3_Tagger(self.__track_number,self.__title,self.__artist,self.__album,
                                   self.__year,self.__genre,self.__language,self.__description,
                                   self.__cover_art,self.__comment)

    def get_edited_info(self):
        self.__metainfo = self.metainfo.MetaInfo(self.__title,self.__artist,self.__year,self.__cover_art,self.__comment)
        return self.__metainfo


    def set_title(self,song_title):
        self.__title = song_title

    def set_file(self,audio_file):
        self.__file = audio_file

    def set_artist(self,song_artist):
        self.__artist = song_artist

    def set_year(self,song_year):
        self.__year = song_year

    def set_cover_art(self,song_cover):
        self.__cover_art = song_cover

    def set_comment(self,song_comment):
        self.__comment = song_comment

    def set_language(self,language):
        self.__language = language

    def set_description(self,description):
        self.__description = description

    def set_track_number(self,track_number):
        self.__track_number = track_number

    def set_album(self,album):
        self.__album = album

    def set_genre(self,genre):
        self.__genre = genre

