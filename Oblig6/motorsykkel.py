class Motorcycle:
    def __init__(self, brand: str,
                 licence_nr: str,
                 distance_driven: int):
        self.brand = brand
        self.licence_nr = licence_nr
        self.distance_driven = distance_driven
    
    def drive(self, km):
        self.distance_driven += km

        return self.distance_driven
    
    def get_distance_driven(self):
        return self.distance_driven
    
    def __str__(self):
        return f'brand: {self.brand}, licence number: {self.licence_nr}, distance driven: {self.distance_driven}'