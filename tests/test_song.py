from song import Song
def test_sanity():
    assert True
def test_song_stores_attributes():
    song=Song("xyz","abc","lorem ipsum")
    assert song.song_id is None
    assert song.title=="xyz"
    assert song.artist=="abc"
    assert song.info=="lorem ipsum"

