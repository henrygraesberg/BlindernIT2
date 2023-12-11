class Dato:
    def __init__(self, ny_dag: int, ny_maaned: int, nytt_aar: int):
        self.dag = ny_dag
        self.maaned = ny_maaned
        self.aar = nytt_aar

    def __str__(self):
        dates = ["jan", "feb", "mar", "apr", "mai", "jun", "jul", "aug", "sep", "okt", "nov", "des"]

        return f'{self.dag}. {dates[self.maaned - 1]} {self.aar}'
    
    def les_aar(self):
        return self.aar
    
    def check_date(self, day: int):
        return self.dag == day
    
    def compare(self, other_date):
        if self.aar == other_date.aar and self.maaned == other_date.maaned and self.dag == other_date.dag:
            return "Datoene er samme"
        if self.aar < other_date.aar:
            return "Self er før"
        if self.aar > other_date.aar:
            return "Self er etter"
        if self.maaned < other_date.maaned:
            return "Self er før"
        if self.maaned > other_date.maaned:
            return "Self er etter"
        if self.dag < other_date.dag:
            return "Self er før"
        if self.dag > other_date.dag:
            return "Self er etter"
    
    def increase_day(self):
        new_day = self.dag + 1
        new_month = self.maaned
        new_year = self.aar
        
        febdays = 28

        if self.aar % 4 == 0:
            febdays = 29

        days = [31, febdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if new_day > days[self.maaned - 1]:
            new_month += 1
            new_day = 1
        if new_month > 12:
            new_month = 1
            new_year += 1

        self.dag = new_day
        self.maaned = new_month
        self.aar = new_year