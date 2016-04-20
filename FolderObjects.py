from SongObjects import *
from os import *
import shutil
import unicodedata


class LibraryFolder:

    messy = False

    def __init__(self, p, c):
        self.path = p
        self.copy = c
        self.songs = []
        self.off_artists = []
        self.off_albums = []
        self.buildFolder()
        self.getSongInfo()




    def addSong(self, song):
        self.songs.append(song)



    def buildFolder(self):
        for subdir, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".mp3"):
                   self.addSong(MP3Song(os.path.join(subdir, file)))
                elif file.endswith(".flac"):
                   self.addSong(FLACSong(os.path.join(subdir, file)))


    def printSongs(self):
        for song in self.songs:
            print song.path



    def getSongInfo(self):
        artists = dict()
        albums = dict()
        for song in self.songs:
            artist = str(song.artist)
            album = str(song.album)
            if artist in artists.keys():
                artists[artist] = artists[artist] + 1
            else:
                artists[artist] = 1
            if album in albums.keys():
                albums[album] = albums[album] + 1
            else:
                artists[album] = 1

        max = 0
        max_artist = ""
        max_album = ""
        for artist in artists.keys():
            count = artists[artist]
            if count > max:
                max_artist = artist
                max = count
        max = 0
        for album in albums.keys():
            count = albums[album]
            if count > max:
                max_album = album
                max = count
        if (self.songs.__len__() / 2) > max:
            self.messy = True
            return False;
        else:
            self.messy = True
            self.album = max_album
            self.artist = max_artist
            return True


    def NormalizeSongInfo(self):

        for song in self.songs:
            if song.artist != self.artist:
                off_artist = song.artist
                if self.artist in off_artist:
                    off_artist.replace(self.artist, "")
                song.setTitle(song.title + ' feat. ' + off_artist)
                song.setArtist(self.artist)
            if song.album != self.album:
                off_album = song.album
                if self.album in off_album:
                    off_album.replace(self.album, "")
                song.setTitle(song.title + ' from ' + off_album)
                song.setAlbum(self.album)


    def makeFolder(self, path):

        if self.messy is True:

            self.makeMessyFolder(path)
        else:
            #self.NormalizeSongInfo()
            self.makeCleanFolder(path)


    def makeCleanFolder(self, folderpath):
        path = folderpath
        path = albumPath = self.pathJoin(path, self.artist)
        if not os.path.exists(path):
            os.makedirs(path)
        albumPath = self.pathJoin(path, self.album)
        if not os.path.exists(albumPath):
            os.makedirs(albumPath)
        if self.copy is True:
            for currSong in self.songs:
                songPath = os.path.split(currSong.path)[1]
                shutil.copy2(currSong.path, self.pathJoin(albumPath, songPath))
        else:
            for currSong in self.songs:
                songPath = os.path.split(currSong.path)[1]
                os.rename(currSong.path, self.pathJoin(albumPath, songPath))

    def makeMessyFolder(self, folderpath):

        for songCurr in self.songs:
            path = folderpath
            path = self.pathJoin(path, (songCurr.artist))
            if not os.path.exists(path):
                os.makedirs(path)

            albumPath = self.pathJoin(path, songCurr.album)
            if not os.path.exists(albumPath):
                os.makedirs(albumPath)
            if self.copy is True:
                songPath = self.pathJoin(albumPath, os.path.split(songCurr.path)[1])
                #if not os.path.exists(songPath):
                print
                shutil.copy2(songCurr.path, songPath)


    def pathJoin(self, path, add):
        add = str(add).replace("/", "-").replace("\\", "-")
        if add.startswith("[u'"):
            add = add[3:-2]
        #unicodedata.normalize('NFKD', add).encode('ascii','ignore')
        return os.path.join(path, add)



