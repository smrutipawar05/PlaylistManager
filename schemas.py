from pydantic import BaseModel
from typing import Optional

class SongCreate(BaseModel):
    title:str
    artist:str
    info:str

class SongUpdate(BaseModel):
    title:Optional[str]=None
    artist:Optional[str]=None
    info:Optional[str]=None

class SongResponse(BaseModel):
    song_id:int
    title:str
    artist:str
    info:str

