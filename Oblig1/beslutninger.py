#Spør om brukeren vil ha en brus, og gir passende svar

def brus():
    #Tar input fra brukeren
    svar = input("Vil du ha en brus? ")

#Sjekker om inputet er ja eller nei med hensyn til stor forbokstav
    if(svar == "ja" or svar == "Ja"):
        print("Her har du en brus! 🥤")
    elif(svar == "nei" or svar == "Nei"):
        print("Den er grei")
    #Hvis inputtet verken er ja eller nei vil funksjonen kjøre igjen
    else:
        print("Det forstod jeg ikke helt")
        brus()

#Kjører funksjonen
brus()