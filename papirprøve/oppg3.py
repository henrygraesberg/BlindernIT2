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