from song import Song
class SongLibrary:
    def __init__(self):
        self.songs_by_name={}
        self.songs_by_id={}
    def add_song(self,song):
        if not isinstance(song,Song):
            raise TypeError("improper argument.")
        key=(song.title,song.artist)
        if key in self.songs_by_name:
            raise ValueError("Song already exists.")
        #self.songs_by_name.update({(song.title,song.artist):song})
        self.songs_by_name[key]=song
        self.songs_by_id[song.song_id]=song
        #cleaner:self.songs[key]=song
    def find_song(self,title,artist):
        key=(title,artist)
        return self.songs_by_name[key]
    def remove_song(self,title,artist):
        #i couldve called find_song right?
        key=(title,artist)
        key_song_id=(self.find_song(title,artist)).song_id
        del self.songs_by_id[key_song_id]
        del self.songs_by_name[key]
    def display_all_songs(self):
        for song in self.songs_by_name.values():
            song.display()
    def find_song_by_id(self,song_id):
        return self.songs_by_id[song_id]