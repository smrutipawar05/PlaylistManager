from song import Song
from schemas import SongResponse
class Mapper:
    # @staticmethod
    # def create_song_to_domain(data):
    #     song=Song(data.title,data.artist,data.info)
    #     return song
    @staticmethod
    def song_to_response(song):
        song_response=SongResponse(
            song_id=song.song_id,
            title=song.title,
            artist=song.artist,
            info=song.info)
        return song_response