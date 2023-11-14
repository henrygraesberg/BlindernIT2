steder = []
klesplagg = []
avreisedatoer = []

for i in range(5):
    steder.append(input("Hvor vil du reise? "))
    klesplagg.append(input("Hva skal du ha på deg når du er det? "))
    avreisedatoer.append(input("Når reiser du? "))

reiseplan = [steder, klesplagg, avreisedatoer]

for i in reiseplan:
    print(i)

liste_index_1 = int(input("Skriv en liste index: "))
liste_index_2 = int(input("Skriv en til liste index: "))

if 0 <= liste_index_1 < len(reiseplan) and 0 <= liste_index_2 < len(reiseplan):
    print(reiseplan[liste_index_1][liste_index_2])
else:
    raise IndexError("index out of range")
