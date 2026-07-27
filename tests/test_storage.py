from SqliteStorage import SQLiteStorage
import sqlite3
from song import Song
def test_storage_initiates():
    storage=SQLiteStorage("file")
    storage.connection=sqlite3.connect("file")
    storage.cursor=storage.connection.cursor()
    storage.cursor.execute("PRAGMA foreign_keys=ON")
    storage.create_tables()
    assert storage.connection
def test_save_song():
    storage=SQLiteStorage(":memory:")
    song=Song("xyz","abc","info")
    storage.save_song(song)
    song_list=storage.load_songs()
    loaded_song=song_list[0]
    assert loaded_song.title==song.title
    assert loaded_song.artist==song.artist
    assert loaded_song.info==song.info