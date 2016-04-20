from SongObjects import *
from FolderObjects import *
rootdir ='C:/Users/JACKIE CHAN/CS/PythonWork/LibraryHelper/TestLib/Disclosure - Settle (2013) [FLAC]'
root ='C:/Users/JACKIE CHAN/CS/PythonWork/LibraryHelper/TestLib/'

for a, b, c in os.walk(root):
    print b


norbor = LibraryFolder(rootdir)

for a in norbor.songs:

    print os.path.split(a.path)[1]


