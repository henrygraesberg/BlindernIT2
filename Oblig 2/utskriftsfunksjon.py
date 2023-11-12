#Ber om navn og bosted 3 ganger og printer ut informasjonen

#Definerer en klasse som inneholder navn og bosted til en person, og 
#har en modifisert __str__ metode for å møte oppgavebestilingen når vi 
#printer informasjonen
class Person:
    def __init__(self, navn: str, bosted: str):
        self.navn = navn
        self.bosted = bosted

    def __str__(self):
        return f'Hei {self.navn}! Du bor i {self.bosted}'

#Instantierer et objekt av klassen Person, og ber om input av navn og 
#bosted, og printer objektet til konsollet, hvor vi matcher 
#oppgavebestillingens formatering takket være den modifiserte __str__
#metoden i objektet
for i in range(3):
    pers = Person(input("Skriv inn navn "), input("Hvor bor du? "))
    print(pers)