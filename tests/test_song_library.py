from song_library import SongLibrary
from song import Song
def test_library_starts():
    library=SongLibrary()
    assert library.songs_by_id=={}
    assert library.songs_by_name=={}
def test_add_song_to_library():
    library=SongLibrary()
    song=Song("xyz","abc","info") 
    library.add_song(song)
    key=(song.title,song.artist)
    assert library.songs_by_name[key]==song
def test_remove_song_from_library():
    library=SongLibrary()
    song1=Song("xyz","abc","info") 
    library.add_song(song1)
    key=(song1.title,song1.artist)
    library.remove_song(song1.title,song1.artist)
    assert key not in library.songs_by_name
def test_find_song_by_name_library():
    library=SongLibrary()
    song1=Song("xyz","abc","info") 
    library.add_song(song1)
    assert library.find_song(song1.title,song1.artist)==song1
def test_find_song_by_id_library():
    library=SongLibrary()
    song1=Song("xyz","abc","info") 
    library.add_song(song1)
    assert library.find_song_by_id(song1.song_id)==song1   