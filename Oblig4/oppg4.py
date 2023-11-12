matplan = {
    "Kari Nordmann": ["brød", "egg", "pølse"],
    "Lars Petterson": ["appelsinjuice", "pizza", "torsk"],
    "Alan Turing": ["calzone", "enchiladas", "paella"]
}

def finn_plan():
    print(matplan.keys())
    user_in = input("Skriv et navn til en beboer: ")

    if user_in in matplan:
        print(matplan[user_in])
    else:
        print("Beboeren er ikke registrert")

finn_plan()

#a: liste, vi trenger kun et brukernavn per plass. Hvis du vil ha navnet på studenten OG brukernavnet, hadde jeg brukt en dict
#b: dict, vi trenger både brukernavn og poeng, da er det best å ha brukernavnet som key, og poengverdien som value
#c: liste, vi trenger bare navnet, ikke noen andre verdier knyttet til navnet, som f.eks. hvor mye de vant, eller når de vant
#d: dict, vi kan knytte navnet som key med hva de er allergisk mot som value