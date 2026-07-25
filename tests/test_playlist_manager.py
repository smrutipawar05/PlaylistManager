from playlistmanager import PlaylistManager
from SqliteStorage import SQLiteStorage
from song_library import SongLibrary
from playlist import Playlist
from song import Song
def test_playlist_manager_starts():
    storage=SQLiteStorage("file_name")
    library=SongLibrary()
    manager=PlaylistManager(storage,library)
    assert manager.storage==storage
    assert manager.library==library
    assert manager.playlists=={}
def test_create_playlist():
    # playlist=Playlist("playlist_name")
    storage=SQLiteStorage(":memory:")
    library=SongLibrary()
    manager=PlaylistManager(storage,library)
    p=manager.create_playlist("playlist_name")
    assert manager.playlists["playlist_name"]==p
def test_find_playlist():
    storage=SQLiteStorage(":memory:")
    library=SongLibrary()
    manager=PlaylistManager(storage,library)
    p1=manager.create_playlist("playlist_name1")
    p2=manager.create_playlist("playlist_name2")
    assert manager.find_playlist("playlist_name2")==p2
def test_add_song_to_library():
    storage=SQLiteStorage(":memory:")
    library=SongLibrary()
    manager=PlaylistManager(storage,library)
    #song=Song("xyz","abc","info")
    song=manager.add_song_to_library("xyz","abc","info")
    key=("xyz","abc")
    assert manager.library.songs_by_name[key]==song
def test_add_song_to_playlist():
    storage=SQLiteStorage(":memory:")
    library=SongLibrary()
    manager=PlaylistManager(storage,library)
    p=manager.create_playlist("playlist_name")
    song=manager.add_song_to_library("xyz","abc","info")
    manager.add_song_to_playlist("playlist_name",song.title,song.artist)
    assert p.songs[0]==song
def test_remove_song_from_playlist():
    storage=SQLiteStorage(":memory:")
    library=SongLibrary()
    manager=PlaylistManager(storage,library)
    p=manager.create_playlist("playlist_name")    
    song=manager.add_song_to_library("xyz","abc","info")
    manager.add_song_to_playlist("playlist_name",song.title,song.artist)
    manager.remove_song_from_playlist("playlist_name",song.title,song.artist)
    key=(song.title,song.artist)
    assert not p.contains_song(song)
def test_find_playlist_by_id():
    storage=SQLiteStorage(":memory:")
    library=SongLibrary()
    manager=PlaylistManager(storage,library)
    p=manager.create_playlist("playlist_name")    
    assert manager.find_playlist_by_id(p.playlist_id)==p
def test_load_library():
    storage=SQLiteStorage(":memory:")
    library1=SongLibrary()
    manager1=PlaylistManager(storage,library1)
    manager1.add_song_to_library("xyz","abc","info")  
    #storage.save_library(library1)
    library2=SongLibrary()
    manager2=PlaylistManager(storage,library2)
    loaded_library=manager2.load_library()
    song=loaded_library.find_song("xyz","abc")
    assert song.title=="xyz"
    assert song.artist=="abc"
def load_playlists():
    storage=SQLiteStorage(":memory:")
    library1=SongLibrary()
    manager1=PlaylistManager(storage,library1)
    song=manager1.add_song_to_library("xyz","abc","info")  
    manager1.add_song_to_playlist("playlist_name",song.title,song.artist)
    p=manager1.find_playlist("playlist_name")
    storage.save_playlist(p)
    library2=SongLibrary()
    manager2=PlaylistManager(storage,library1)
    loaded_library=manager2.load_library()
    load_playlists=manager2.load_playlists()
    