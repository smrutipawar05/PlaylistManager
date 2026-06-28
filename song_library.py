from song import Song
class SongLibrary:
    def __init__(self):
        self.songs={}
    def add_song(self,song):
        if not isinstance(song,Song):
            raise TypeError("improper argument.")
        key=(song.title,song.artist)
        if key in self.songs:
            raise ValueError("Song already exists.")
        self.songs.update({(song.title,song.artist):song})
        #cleaner:self.songs[key]=song
    def find_song(self,title,artist):
        key=(title,artist)
        return self.songs[key]
    def remove_song(self,title,artist):
        #i couldve called find_song right?
        key=(title,artist)
        del self.songs[key]
    def display_all_songs(self):
        for song in self.songs.values():
            song.display()