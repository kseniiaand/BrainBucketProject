"""Define a class Songs, it will show the lyrics of a song.
Its __init__() method should have two arguments:self and lyrics.
lyrics is a list. Inside your class create a method called sing_me_a_song()
that prints each element of lyrics on its own line.

"""
class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

ChristmasSong = Songs(["All I want for Christmas",
"is my two front teeth,",
"my two front teeth,",
"see my two front teeth!",
"Gee, if I could only",
"have my two front teeth,",
"then I could with you",
"Merry Christmas.",
"It seems so long since I could say,",
"Sister Susie sitting on a thistle!"])
ChristmasSong.sing_me_a_song()
