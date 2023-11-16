def gangetabell(kollonner: int, rader: int):
    output = []

    for i in range(1, rader + 1):
        rad = []

        for n in range(1, kollonner + 1):
            rad.append(i * n)
        
        output.append(rad)

    return output

print(gangetabell(3, 2))
print(gangetabell(10, 10))