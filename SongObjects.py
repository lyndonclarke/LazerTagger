
import os
from mutagen.flac import FLAC
from mutagen.id3 import ID3, TIT2
from mutagen.easyid3 import EasyID3



class MP3Song():

    def __init__(self, p):
        self.path = p
        self.audio = EasyID3(p)
        self.artist = self.audio['artist']
        self.title = self.audio['title']
        self.album = self.audio['album']
        self.audio.save()

    def setArtist(self, new_artist):
        self.audio['aritst'] = new_artist
        self.artist = new_artist
        self.audio.save()

    def setAlbum(self, new_album):
        self.audio['album'] = new_album
        self.album = new_album
        self.audio.save()

    def setTitle(self, new_title):
        self.audio['title'] = new_title
        self.title = new_title
        self.audio.save()

    def getArtist(self):
        return self.artist

    def getAlbum(self):
        return self.album

    def getTitle(self):
        return self.title

    def getAudio(self):
        return self.audio




class FLACSong():

    def __init__(self, p):
        self.path = p
        self.audio = FLAC(p)

        self.artist = self.audio['artist']
        self.title = self.audio['title']
        self.album = self.audio['album']
        self.audio.save()

    def setArtist(self, new_artist):
        self.audio['aritst'] = new_artist
        self.artist = new_artist
        self.audio.save()

    def setAlbum(self, new_album):
        self.audio['album'] = new_album
        self.album = new_album
        self.audio.save()

    def setTitle(self, new_title):
        self.audio['title'] = new_title
        self.title = new_title
        self.audio.save()

    def getArtist(self):
        return self.artist

    def getAlbum(self):
        return self.album

    def getTitle(self):
        return self.title

    def getAudio(self):
        return self.audio



































