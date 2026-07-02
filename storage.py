from song import Song
from song_library import SongLibrary
from playlist import Playlist
from playlistmanager import PlaylistManager
import json
class Storage:  
    def load(self):
        raise NotImplementedError
    def song_to_dict(self,song):
        return {
            "song_id":song.song_id,
            "title":song.title,
            "artist":song.artist,
            "info":song.info
        }
    def library_to_dict(self,library):
        library_return=[]
        for song in library.songs_by_name.values():
           song_to_list=self.song_to_dict(song)
           library_return.append(song_to_list)
        return {
            "songs":library_return
        }
    def playlist_to_dict(self,playlist):
        playlist_return=[]
        for song in playlist.songs:
            playlist_return.append(song.song_id)
        return {
            "playlist_name":playlist.playlist_name,
            "song_ids":playlist_return
        }
    def manager_to_dict(self,manager):
        manager_playlist_return=[]
        for playlist in manager.playlists.values():
            manager_playlist_return.append(self.playlist_to_dict(playlist))
        return {
            "playlists":manager_playlist_return,
            "library":self.library_to_dict(manager.library)
        }
    def save(self,manager):
        data=self.manager_to_dict(manager)

        with open("playlists.json","w") as file:
            json.dump(data,file)
    def dict_to_song(self,song_data):
        return Song(
            song_data["song_id"],
            song_data["title"],
            song_data["artist"],
            song_data["info"]
        )
    def dict_to_library(self,library_data):
        library=SongLibrary()
        for song_data in library_data["songs"]:
            library.add_song(self.dict_to_song(song_data))
        return library
    def dict_to_playlist(self,playlist_data,library):
        playlist=Playlist(playlist_data["playlist_name"])
        for song_id in playlist_data["song_ids"]:
            song=library.find_song_by_id(song_id)
            playlist.add_song(song)
        return playlist
    def dict_to_manager(self,manager_data):
        manager=PlaylistManager()
        manager.library=self.dict_to_library(manager_data["library"])
        for playlists_list in manager_data["playlists"]:
            playlist=self.dict_to_playlist(playlists_list,manager.library)
            manager.playlists[playlist.playlist_name]=playlist
        return manager
    def load(self):
        with open("playlists.json","r") as file:      
            manager_data=json.load(file)  
            manager=self.dict_to_manager(manager_data)
        return manager