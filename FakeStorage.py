from storage import Storage
class FakeStorage(Storage):
    def __init__(self):
        self.songs={}
        self.next_song_id=1
    def save_song(self,song):
        song.song_id=self.next_song_id
        self.songs[song.song_id]=song
        self.next_song_id+=1
        return song
    def load_songs(self):
        return self.list_songs()
    def list_songs(self):
        return list(self.songs.values())
    def delete_song(self,song_id):
        del self.songs[song_id]
    def update_song(self,song):
        self.songs[song.song_id]=song
    def find_song_by_name(self,title,artist):
        for song in self.songs.values():
            if song.title==title and song.artist==artist:
                return song
        return None
    def get_song(self,song_id):
        return self.songs.get(song_id)