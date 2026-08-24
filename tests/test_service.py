import pytest
from SqliteStorage import SQLiteStorage
from song_service import SongService
from exceptions import SongNotFound,SongAlreadyExists
from schemas import SongUpdate
from FakeStorage import FakeStorage
def test_song_created():
    storage=FakeStorage()
    service=SongService(storage)
    song=service.create_song("xyz","abc","justrandoshit")
    assert song.title=="xyz"
    assert song.artist=="abc"
    assert song.info=="justrandoshit"
def test_get_song():
    storage=FakeStorage()
    service=SongService(storage)
    song=service.create_song("xyz","abc","justrandoshit")
    found_song= service.get_song(song.song_id)
    assert found_song.song_id==song.song_id
    with pytest.raises(SongNotFound):
        service.get_song(2)
def test_list_songs():
    storage=FakeStorage()
    service=SongService(storage)
    song1=service.create_song("xyz","abc","justrandoshit")
    song2=service.create_song("xyz`","abc`","justrandoshitparttwooooooooo")
    songs=service.list_songs()
    assert len(songs)==2
    assert songs[0].song_id==song1.song_id
    assert songs[1].song_id==song2.song_id
def test_update_songs():
    storage=FakeStorage()
    service=SongService(storage)
    song1=service.create_song("xyz","abc","justrandoshit")
    song2=service.create_song("xyz`","abc`","justrandoshitparttwooooooooo")
    update=SongUpdate(info="Changeddd")
    duplicate_update=SongUpdate(title="xyz`",artist="abc`",info="noooooo")
    updated_song=service.update_song(song1.song_id,update)
    assert updated_song.info=="Changeddd"
    with pytest.raises(SongNotFound):
        service.update_song(3,update)
    with pytest.raises(SongAlreadyExists):
        service.update_song(1,duplicate_update)
    song_after=service.get_song(song1.song_id)
    assert song_after.title=="xyz"
    assert song_after.artist=="abc"
    assert song_after.info=="Changeddd"
def test_delete_songs():
    storage=FakeStorage()
    service=SongService(storage)
    song1=service.create_song("xyz","abc","justrandoshit")
    song2=service.create_song("xyz`","abc`","justrandoshitparttwooooooooo")
    deleted_song=service.delete_song(song1.song_id)
    assert deleted_song.song_id==song1.song_id
    assert deleted_song.title=="xyz"
    assert deleted_song.artist=="abc"
    with pytest.raises(SongNotFound):
        service.get_song(song1.song_id)