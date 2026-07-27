from SqliteStorage import SQLiteStorage
import sqlite3
from song import Song
from playlist import Playlist
from playlistmanager import PlaylistManager
from song_library import SongLibrary
import pandas as pd
def test_storage_initiates():
    storage=SQLiteStorage(":memory:")
    assert storage.connection is not None
    assert storage.cursor is not None
def test_save_song():
    storage=SQLiteStorage(":memory:")
    song=Song("xyz","abc","info")
    storage.save_song(song)
    song_list=storage.load_songs()
    loaded_song=song_list[0]
    assert loaded_song.title==song.title
    assert loaded_song.artist==song.artist
    assert loaded_song.info==song.info
    assert loaded_song.song_id==song.song_id
def test_load_songs():
    storage=SQLiteStorage(":memory:")
    song1=Song("xyz","abc","info")
    song2=Song("xyz`","abc`","info`")
    storage.save_song(song1)
    storage.save_song(song2)
    song_list=storage.load_songs()
    loaded_song1=song_list[0]
    loaded_song2=song_list[1]
    assert loaded_song1.title==song1.title
    assert loaded_song2.title==song2.title
    assert loaded_song1.song_id==song1.song_id
    assert loaded_song2.sond_is==song2.song_id
def test_save_playlist():
    storage=SQLiteStorage(":memory:")
    playlist=Playlist("p_name")
    storage.save_playlist(playlist)
    playlist_list=storage.load_playlists()
    loaded_playlist_1=playlist_list[0]
    assert loaded_playlist_1.name()==playlist.name()
    assert loaded_playlist_1.playlist_id==playlist.playlist_id
def test_load_playlist():
    storage=SQLiteStorage(":memory:")
    playlist1=Playlist("p_name")
    playlist2=Playlist("p_name`")
    storage.save_playlist(playlist1)
    storage.save_playlist(playlist2)
    playlist_list=storage.load_playlists()
    loaded_playlist_1=playlist_list[0]
    loaded_playlist_2=playlist_list[1]
    assert loaded_playlist_1.name()==playlist1.name()
    assert loaded_playlist_2.name()==playlist2.name()
    assert loaded_playlist_1.playlist_id==playlist1.playlist_id
    assert loaded_playlist_2.playlist_id==playlist2.playlist_id    
def test_save_playlist_song():
    storage=SQLiteStorage(":memory:")
    library=SongLibrary()
    manager=PlaylistManager(storage,library)
    playlist=manager.create_playlist("p_name")
    song=manager.add_song_to_library("xyz","abc","info")
    pos=manager.add_song_to_playlist(playlist.name(),song.title,song.artist)
    realtion_list=storage.load_playlist_songs()
    relation=realtion_list[0]
    assert relation[0]==playlist.playlist_id
    assert relation[1]==song.song_id
    assert relation[2]==pos
def test_save_playlist_song_independently():
    storage=SQLiteStorage(":memory:")
    playlist=Playlist("p_name")
    song=Song("xyz","abc","info")
    pos=playlist.add_song(song)
    storage.save_playlist(playlist)
    storage.save_song(song)
    storage.save_playlist_song(playlist.playlist_id,song.song_id,pos)
    realtion_list=storage.load_playlist_songs()
    relation=realtion_list[0]
    assert relation[0]==playlist.playlist_id
    assert relation[1]==song.song_id
    assert relation[2]==pos
