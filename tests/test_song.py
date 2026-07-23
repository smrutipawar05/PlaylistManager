from song import Song
from playlist import Playlist
def test_sanity():
    assert True
def test_song_stores_attributes():
    song=Song("xyz","abc","info")
    assert song.song_id is None
    assert song.title=="xyz"
    assert song.artist=="abc"
    assert song.info=="info"
def test_song_returns_values():
    song=Song("xyz","abc","info")
    assert song.values()==(
        "xyz",
        "abc",
        "info"
    )
