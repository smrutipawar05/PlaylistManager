from song import Song
from song_library import SongLibrary
from playlist import Playlist
class PlaylistManager:
    def __init__(self):
        self.library=SongLibrary()
        self.playlists={}
    def create_playlist(self,playlist_name):
        if playlist_name in self.playlists:
            raise ValueError("A playlsit with same name exists.")
        p=Playlist(playlist_name)
        self.playlists.update({playlist_name:p})
        return p
    def find_playlist(self,playlist_name):
        key=playlist_name
        return self.playlists[key]
    def delete_playlist(self,playlist_name):
        del self.playlists[playlist_name]
    def add_song_to_playlist(self,playlist_name,title,artist):
        p=self.find_playlist(playlist_name)
        s=self.library.find_song(title,artist)
        p.add_song(s)
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
    def add_song_to_library(self,song_id,title,info,artist):
        s=Song(song_id,title,artist,info)
        self.library.add_song(s)
    def display_playlist(self,playlist_name):
        p=Playlist(playlist_name)
        p.display()
    def display_song_library(self):
        self.library.display_all_songs()