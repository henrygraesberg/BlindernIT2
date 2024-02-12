from sang import Sang

class Spilleliste:
    def __init__(self, listenavn: str):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        file = open(filnavn, "r")

        for line in file:
            title, artist = line.strip().split(";")

            self._sanger.append(Sang(artist, title))

    def leggTilSang(self, nySang: Sang):
        self._sanger.append(nySang)

    def fjernSang(self, sang: Sang):
        indexof = None

        for song in self._sanger:
            if song.sjekkArtistOgTittel(sang._artist, sang._title):
                indexof = self._sanger.index(song)
                break

        if indexof is not None:
            self._sanger.pop(indexof)

    def spillSang(self, sang: Sang):
        indexof = None

        for song in self._sanger:
            if song.sjekkArtistOgTittel(sang._artist, sang._title):
                indexof = self._sanger.index(song)
        
        if indexof is not None:
            self._sanger[indexof].spill()

    def spillAlle(self):
        for i in self._sanger:
            i.spill()
    
    def finnSang(self, title) -> Sang or None:
        for i in range(len(self._sanger)):
            if self._sanger[i].sjekkTittel(title):
                return self._sanger[i]
            
        return None
    
    def hentArtistUtvalg(self, artist) -> "list[Sang]":
        songs = []
        
        for i in range(len(self._sanger)):
            if self._sanger[i].sjekkArtist(artist):
                songs.append(self._sanger[i])
            
        return songs
