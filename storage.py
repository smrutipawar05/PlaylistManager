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
        for song in library.songs.values():
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
    