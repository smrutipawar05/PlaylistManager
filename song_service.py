from song import Song
from SqliteStorage import SQLiteStorage
from exceptions import SongNotFound,SongAlreadyExists
from schemas import SongUpdate
class SongService:
    def __init__(self,storage):
        self.storage=storage
    def create_song(self,title,artist,info):
        song=Song(title,artist,info)
        self.storage.save_song(song)
        return song 
    def get_song(self,song_id):
        song=self.storage.get_song(song_id)
        if song is None:
            raise SongNotFound()
        return song
    def list_songs(self):
        return self.storage.load_songs()
    def update_song(self,song_id,update):
        song=self.get_song(song_id)
        new_title=update.title if update.title is not None else song.title
        new_artist=update.artist if update.artist is not None else song.artist
        existing_song=self.storage.find_song_by_name(new_title,new_artist)
        if existing_song is not None and existing_song.song_id!=song_id:
            raise SongAlreadyExists()
        if update.title is not None:
            song.title=update.title
        if update.artist is not None:
            song.artist=update.artist
        if update.info is not None:
            song.info=update.info
        self.storage.update_song(song)
        return song
    def delete_song(self,song_id):
        song=self.get_song(song_id)
        self.storage.delete_song(song_id)
        return song
# storage=SQLiteStorage(":memory:")
# service=SongService(storage)
# song=service.create_song("xyz","abc","uhhhhsureee")
# song2=service.create_song("xyz`","abc`","nothinggg")
# print(song.__dict__)
# song_found=service.get_song(1)
# print(song_found.__dict__)
# update=SongUpdate(info="CHANGEDDDDD")
# song_update=service.update_song(1,update)
# print(song_update.__dict__)
# deleted_song=service.delete_song(1)
# song_found=service.get_song(1)
# print(song_found.__dict__)