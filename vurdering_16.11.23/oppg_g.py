def fil_til_liste(filnavn: str):
    fil = open(filnavn)

    output = []

    for linje in fil:
        output.append(linje.strip())

    print(output)
    return output

navneliste = fil_til_liste("navn.txt")