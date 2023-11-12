#Sjekker hvilken rekkefølge to datoer er i

#Tar input av den første datoen
date1d = input("Dato 1 dag: ")
date1m = input("Dato 1 måned: ")

#Tar input av den andre datoen
date2d = input("Dato 2 dag: ")
date2m = input("Date 2 måned: ")

#Sjekker om dato to kommer før dato en. Hvis begge sjekkene returnerer false,
#kommer dato en før dato to, og vi printer "riktig rekkefølge"
monthcheck = date2m < date1m
daycheck = date2m == date1m and date2d < date1d

if(monthcheck or daycheck):
    print("Feil rekkefølge")
else:
    print("Riktig rekkefølge")