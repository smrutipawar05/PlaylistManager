from song import Song
from playlist import Playlist
def test_playlist_returns_name():
    playlist=Playlist("playlist_name_xyz")
    assert playlist.name()==playlist.playlist_name
def test_playlist_starts():
    playlist=Playlist("playlist_name_xyz")
    assert playlist.playlist_id is None
    assert playlist.songs==[]
    assert playlist.playlist_name=="playlist_name_xyz"
def test_playlist_add_songs():
    playlist=Playlist("playlist_name_xyz")
    song=Song("xyz","abc","info")
    playlist.add_song(song)
    assert len(playlist.songs)==1
    assert playlist.songs[0]==song
def test_playlist_preserve_order():
    playlist=Playlist("playlist_name_xyz")
    song1=Song("xyz","abc","info") 
    song2=Song("`xyz","`abc","`info") 
    playlist.add_song(song1)
    playlist.add_song(song2)
    assert playlist.songs==[song1,song2]
def test_playlist_remove_songs():
    playlist=Playlist("playlist_name_xyz")
    song1=Song("xyz","abc","info") 
    song2=Song("`xyz","`abc","`info") 
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.remove_song(song1)
    assert len(playlist.songs)==1
    assert playlist.songs[0]==song2
def test_playlist_contain_songs():
    playlist=Playlist("playlist_name_xyz")
    song1=Song("xyz","abc","info") 
    song2=Song("`xyz","`abc","`info") 
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.remove_song(song2)
    assert playlist.contains_song(song1)
    assert not playlist.contains_song(song2)
