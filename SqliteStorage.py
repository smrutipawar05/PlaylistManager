import sqlite3
from storage import Storage
from song import Song
from playlist import Playlist

class SQLiteStorage(Storage):
    def __init__(self,file_name):
        self.file_name=file_name
        self.connection=sqlite3.connect(file_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys= ON")
        self.create_tables()
    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Songs(
                    song_id INTEGER PRIMARY KEY,            
                    title text,
                    artist text,
                    info text                            
                );
        ''')
        self.playlist_table()
        self.playlist_song_table()
        self.connection.commit()
    def save_song(self,song):
        SQL='''INSERT INTO Songs
               (title,artist,info)
               Values(?,?,?)'''
        self.cursor.execute(SQL,song.values())
        song.song_id=self.cursor.lastrowid
        self.connection.commit()
    def save_library(self,library):
        for song in library.songs_by_name.values():
            self.save_song(song)
    def load_songs(self):
        SongObject_list=[]
        self.cursor.execute('''SELECT * FROM Songs ''')
        rows=self.cursor.fetchall()
        for row in rows:
            title=row[1]
            artist=row[2]
            info=row[3]  
            s=Song(title,artist,info)
            s.song_id=row[0]
            SongObject_list.append(s)
        return SongObject_list
    def playlist_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Playlists(
            playlist_id INTEGER PRIMARY KEY,
            playlist_name TEXT UNIQUE);
        ''')
        self.connection.commit()
    def playlist_song_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS PlaylistSongs(
                            playlist_song_id INTEGER PRIMARY KEY,
                            playlist_id INTEGER NOT NULL,
                            song_id INTEGER NOT NULL,
                            position INTEGER NOT NULL,
                            FOREIGN KEY(playlist_id)
                                REFERENCES Playlists(playlist_id)
                                ON DELETE CASCADE,
                            FOREIGN KEY(song_id)
                                REFERENCES Songs(song_id)
                            );''')
    def save_playlist(self,playlist):
        SQL='''INSERT INTO Playlists
                (playlist_name)
                VALUES(?);'''
        self.cursor.execute(SQL,(playlist.name(),))
        playlist.playlist_id=self.cursor.lastrowid
        self.connection.commit()
    def save_playlist_song(self,playlist_id,song_id,position):
        SQL='''INSERT INTO PlaylistSongs
            (playlist_id,song_id,position)
            VALUES(?,?,?)'''
        self.cursor.execute(SQL,(playlist_id,song_id,position))
        self.connection.commit()
    def load_playlists(self):
        playlistObject_list=[]
        self.cursor.execute('''SELECT * FROM Playlists''')
        rows=self.cursor.fetchall()
        for row in rows:
            playlist_id=row[0]
            playlist_name=row[1]
            playlist=Playlist(playlist_name)
            playlist.playlist_id=playlist_id
            playlistObject_list.append(playlist)
        return playlistObject_list
    def load_playlist_songs(self):
            relations=[]
            self.cursor.execute('''SELECT * FROM PlaylistSongs''')
            rows=self.cursor.fetchall()
            for row in rows:
                playlist_id=row[1]
                song_id=row[2]
                position=row[3]
                relation=(playlist_id,song_id,position)
                relations.append(relation)
            return relations
    def delete_playlist(self,playlist_name):
        SQL='''DELETE FROM Playlists
            WHERE playlist_name=?'''
        self.cursor.execute(SQL,(playlist_name,))
        self.connection.commit()
            