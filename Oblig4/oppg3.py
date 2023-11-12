fruktliste  = ["eple", "eple", "banan", "banan", "banan"]
fruktmengde = {"eple", "eple", "banan", "banan", "banan"}

#False blir printet, siden fruktmengde er en dictionary, og man kan bare
#ha en av hver key i ett dictionary. Det eksta "eple" og de to ekstra
#"banan" blir ignorert. Vi sammenlikner derfor 5 og 2, og de er ikke like
print(len(fruktliste) == len(fruktmengde))

frukt_dict = {
    "eple": 2,
    "banan": 3
}

print(frukt_dict)

frukt_in = input("Skriv en frukt: ").lower
antall_in = int(input("Skriv hvor mange av frukten"))

if antall_in < 0:
    print("Ugyldig input!")
elif frukt_in in frukt_dict:
    frukt_dict[frukt_in] += antall_in
else:
    frukt_dict[frukt_in] = antall_in

print(frukt_dict)