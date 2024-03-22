import gjest

class Rorbu:
    def __init__(self) -> None:
        self._gjester = []
    
    def legg_til_gjest(self, ny_gjest: gjest.Gjest) -> None:
        for gjest in self._gjester:
            gjest.underhold(1)
        
        self._gjester.append(ny_gjest)
    
    def fortell_vits(self, morsomhet: int) -> None:
        for gjest in self._gjester:
            gjest.underhold(morsomhet)
    
    def hvor_morsomt_har_vi_det(self) -> str:
        sum_morsomt = 0

        for gjest in self._gjester:
            sum_morsomt += gjest.hent_underholdningsverdi()
        
        average = sum_morsomt/len(self._gjester)

        if average < 400:
            return "Kjedelig kveld" if average < 200 else "Dette var jo litt gøy"
        else:
            return "Dette var artig" if average < 600 else "Dra til Lopphavet - bi dæ godtar no så gyt e!"
