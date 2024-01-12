class Sang:
    def __init__(self, artist: str, title: str):
        self._artist = artist
        self._title = title

    def spill(self):
        print(f'Spiller {self._title} av {self._artist}')

    def sjekkArtist(self, name: str) -> bool:
        seperate_names = name.split()
        seperate_artists = self._artist.split()

        for i in seperate_names:
            if i in seperate_artists:
                return True
            
        return False
    
    def sjekkTittel(self, title: str) -> bool:
        title = title.lower()
        if title == self._title.lower():
            return True
        
        return False
    
    def sjekkArtistOgTittel(self, artist: str, title: str) -> bool:
        return self.sjekkArtist(artist) and self.sjekkTittel(title)