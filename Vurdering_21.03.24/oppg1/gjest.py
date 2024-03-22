class Gjest:
    def __init__(self) -> None:
        self._underholdningsverdi = 0
    
    def hent_underholdningsverdi(self) -> int:
        return self._underholdningsverdi
    
    def underhold(self, verdi: int) -> None:
        self._underholdningsverdi += verdi