class Song:
    def __init__(self,title,artist,info):
        self.song_id=None
        self.title=title
        self.artist=artist
        self.info=info
    def display(self):
        print(f"ID:{self.song_id}")
        print(f"Title:{self.title}")
        print(f"Artist:{self.artist}")
        print(f"Info:{self.info}")
    def values(self):
        return(
            # self.song_id,
            self.title,
            self.artist,
            self.info
        )

#s1=Song(1,"Believer","Imagine Dragons","Rock")
#s1.display()  