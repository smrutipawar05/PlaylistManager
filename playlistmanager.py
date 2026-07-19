from song import Song
# from song_library import SongLibrary
from playlist import Playlist
# from SqliteStorage import SQLiteStorage
class PlaylistManager:
    def __init__(self,storage,library):
        self.storage=storage
        self.library=library
        self.playlists={}
    def create_playlist(self,playlist_name):
        if playlist_name in self.playlists:
            raise ValueError("A playlsit with same name exists.")
        p=Playlist(playlist_name)
        self.playlists.update({playlist_name:p})
        self.storage.save_playlist(p)
        return p
    def find_playlist(self,playlist_name):
        key=playlist_name
        return self.playlists[key]
    def delete_playlist(self,playlist_name):
        self.storage.delete_playlist(playlist_name)
        del self.playlists[playlist_name]
    def add_song_to_playlist(self,playlist_name,title,artist):
        p=self.find_playlist(playlist_name)
        s=self.library.find_song(title,artist)
        position=p.add_song(s)
        self.storage.save_playlist_song(p.playlist_id,s.song_id,position)
    def remove_song_from_playlist(self,playlist_name,title,artist):
        p=self.find_playlist(playlist_name)
        s=self.library.find_song(title,artist)
        p.remove_song(s)
    def display_all_playlist(self):
        if not self.playlists:
            print("No playlists found.")
            return
        for key in self.playlists:
            print(key)
    def add_song_to_library(self,title,artist,info):
        s=Song(title,artist,info)
        self.library.add_song(s)
        self.storage.save_song(s)
    def display_playlist(self,playlist_name):
        p=self.find_playlist(playlist_name)
        p.display()
    def display_song_library(self):
        self.library.display_all_songs()
    def load_library(self):
        songs=self.storage.load_songs()
        for song in songs:
            self.library.add_song(song)
    def find_playlist_by_id(self,playlist_id):
        for playlist in self.playlists.values():
            if playlist_id==playlist.playlist_id:
                return playlist
    def load_playlists(self):
        playlists=self.storage.load_playlists()
        for playlist in playlists:
            self.playlists[playlist.name()]=playlist
    def load_playlist_songs(self):
        playlists_songs=self.storage.load_playlist_songs()
        for playlist_id,song_id,position in playlists_songs:
            playlist=self.find_playlist_by_id(playlist_id)
            song=self.library.find_song_by_id(song_id)
            playlist.add_song(song)

    