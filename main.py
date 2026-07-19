from playlistmanager import PlaylistManager
from SqliteStorage import SQLiteStorage
from song_library import SongLibrary
storage=SQLiteStorage("playlist.db")
library=SongLibrary()
pm=PlaylistManager(storage,library)
pm.load_library()
pm.load_playlists()
pm.load_playlist_songs()
while True:
    print("-------------PlaylistManager---------------")
    print( '''
    Song Library
    ───────────────────────────────────────────────
    1. Add Song
    2. View Song Library

    Playlist Management
    ───────────────────────────────────────────────
    3. Create Playlist
    4. View All Playlists
    5. View Playlist
    6. Delete Playlist

    Playlist Operations
    ───────────────────────────────────────────────
    7. Add Song to Playlist
    8. Remove Song from Playlist

    System
    ───────────────────────────────────────────────
    9. Exit

    ───────────────────────────────────────────────
    Enter your choice: ''')
    try:
        choice=int(input())
    except ValueError:
        print("PLease enter a number")
        continue
    if choice==1:
        title=input("Enter title of the song")
        artist=input("Enter artist of the song")
        info=input("Enter song info")
        try:
            pm.add_song_to_library(
                # song_id,
                title,
                artist,
                info
            )
            # song_id+=1
        except TypeError:
            print("Imporper format.")
        except ValueError:
            print("Song already exists.")
    elif choice==2:
        pm.display_song_library()
    elif choice==3:
        playlist_name=input("Enter playlist name")
        try:
            pm.create_playlist(playlist_name)
        except ValueError:
            print("A playlist with the same name exists.")
    elif choice==4:
        pm.display_all_playlist()
    elif choice==5:
        playlist_name_find=input("Enter playlist name to view")
        try:
            pm.display_playlist(playlist_name_find)
        except KeyError:
            print("Playlist not found.")
    elif choice==6:
        playlist_name_del=input("enter playlist name to delete")
        try:
            pm.delete_playlist(playlist_name_del)
        except KeyError:
            print("Playlist not found.")
    elif choice==7:
        playlist_name=input("Enter the playlist name")
        title=input("Enter title of the song")
        artist=input("Enter artist of the song")
        try:
            pm.add_song_to_playlist(
                playlist_name,
                title,
                artist
            )
        except KeyError:
            print("Playlslit not found.")
    elif choice==8:
        playlist_name=input("Enter the playlist name")
        title=input("Enter title of the song")
        artist=input("Enter artist of the song")
        try:
            pm.remove_song_from_playlist(
                playlist_name,
                title,
                artist
            )
        except KeyError:
            print("Playlsit not found.")
    elif choice==9:
        break
    else:
        print("Invalid input.")