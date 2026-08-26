import fastAPI
from schemas import SongCreate
from mapper import Mapper
def create_router(service):
    router=APIRouter()

    @router.post("/songs")
    def create_song(data: SongCreate):
        song=service.create_song(data.title,data.artist,data.info)
        return Mapper.song_to_response(song)
    return router
