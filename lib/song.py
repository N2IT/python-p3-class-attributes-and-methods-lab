class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genre(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)


    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genre(cls, self):
        cls.genres.append(self.genre)
        
    @classmethod
    def add_to_artists(cls, self):
        cls.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls, self, increment = 1):
        breakpoint()
        g_count = 0
        cls.genre_count = {
                    self.genre : 1
                } 
        # g_count = 0
        # for genres in cls.genres:
        #     if genres == self.genre:
        #         breakpoint()
        #         cls.genre_count[value] = cls.genre_count[value] + increment
        #     else:
        #         genre_count = {
        #             self.genre : sum(g_count + increment)
                # } 


        # adds to genre_count where keys are names of each genre
        # each key points to a value that is the number of songs assigned to that genre
        
    @classmethod
    def add_to_artist_count(cls, self):
        pass
