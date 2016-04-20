__author__ = 'JACKIE CHAN'
import os
from mutagen.flac import FLAC
from SongObjects import *
from FolderObjects import *



rootdir ='C:/Users/JACKIE CHAN/CS/PythonWork/LibraryHelper/TestLib/'


def indexPath(path):
    folders = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".mp3") or file.endswith(".flac"):
                folder = LibraryFolder(subdir, True)
                folders.append(folder)
                break
    return folders





def buildCleanLibrary(newLib, oldLib):
    if not os.path.exists(newLib):
        os.makedirs(newLib)
    folders = indexPath(oldLib)

    for folder in folders:
        folder.makeFolder(newLib)

buildCleanLibrary('C:/Users/JACKIE CHAN/CS/PythonWork/LibraryHelper/newlib',rootdir, )



