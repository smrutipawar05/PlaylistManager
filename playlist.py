from song import Song
class Playlist:
    def __init__(self,playlist_name):
        self.playlist_name=playlist_name
        self.songs=[]
    def add_song(self,song):
        if not isinstance(song,Song):
            raise TypeError("Improper argument.")
        self.songs.append(song)
    def remove_song(self,song):
        self.songs.remove(song)
    def contains_song(self,song):
        return song in self.songs
    def display(self):
        for song in self.songs:
            song.display()
    