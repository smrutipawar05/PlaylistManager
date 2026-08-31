from fastapi import APIRouter,HTTPException
from schemas import SongCreate,SongUpdate
from mapper import Mapper
from exceptions import SongNotFound,SongAlreadyExists
def create_router(service):
    router=APIRouter()
    @router.post("/songs")
    def create_song(data: SongCreate):
        song=service.create_song(data.title,data.artist,data.info)
        return Mapper.song_to_response(song)
    @router.get("/songs")
    def load_songs():
        songs=service.list_songs()
        return [Mapper.song_to_response(song) for song in songs]
    @router.get("/song/{song_id}")
    def load_song(song_id:int):
        try:
            song=service.get_song(song_id)
            return Mapper.song_to_response(song)
        except SongNotFound:
            raise HTTPException(
                status_code=404,
                detail="Song Not Found."
            )
    @router.patch("/song/{song_id}")
    def update_song(song_id:int, song_update:SongUpdate):
        try:
            song=service.update_song(song_id,song_update)
            return Mapper.song_to_response(song)
        except SongNotFound:
            raise HTTPException(
                status_code=404,
                detail="Song Not Found."
            )
        except SongAlreadyExists:
            raise HTTPException(
                status_code=409,
                detail="Song Already Exists."
            )
    @router.delete("/song/song_id")
    def delete_song(song_id:int):
        try:
            song=service.delete_song(song_id)
            return song 
        except SongNotFound:
            raise HTTPException(
                status_code=404,
                detail="Song Not Found."
            )
    return router