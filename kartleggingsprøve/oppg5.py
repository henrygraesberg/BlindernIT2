liste = ["I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så",
         "lykkelig", "det", "hele", "endte", "dejligt", "og", "er", "glad",
         "Ja", "alting", "endte", "lykkeligt", "så", "lykkeligt", "i", "dag",
         "er", "jeg", "så", "lykkelig", "som", "dagen", "er", "lang"]

print(len(liste))

antall = {
    "lykkelig": 0,
    "så": 0,
    "dag": 0
}

for i in liste:
    if i == "lykkelig":
        antall["lykkelig"] += 1
    elif i == "så":
        antall["så"] += 1
    elif i == "dag":
        antall["dag"] += 1
        
print(antall)