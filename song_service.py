from song import Song
class SongService:
    def __init__(self,storage):
        self.storage=storage
    def create_song(self,title,artist,info):
        song=Song()