def tell_forekomst(ord1: str, ord2: str, bokstav: chr):
    count1, count2 = 0, 0

    for l in ord1:
        if l == bokstav:
            count1 += 1
    for l in ord2:
        if l == bokstav:
            count2 += 1
        
    if count1 > count2:
        return ord1
    if count2 > count1:
        return ord2
    return "likt"

print(tell_forekomst("banan", "alle", "a"))

def tell_forekomst(ord: str, bokstav: chr):
    count = 0

    for l in ord:
        if l == bokstav:
            count += 1
    
    return count

class Russebuss:
    def __init__(self, plasser: int, antall_personer: int):
        self.plasser = plasser
        self.antall_personer = antall_personer

    def get_personer(self):
        return self.antall_personer

    def slipp_på(self, antall_personer):
        if self.plasser <= self.antall_personer + antall_personer:
            self.antall_personer = self.plasser
            return "Bussen er full"

        self.antall_personer += antall_personer
