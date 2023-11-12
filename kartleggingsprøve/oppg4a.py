user_in = int(input("Skriv et heltall"))

if user_in < 0:
    print("Error: Number cannot be negative")
else:
    i = 0
    while i <= user_in:
        print(i)
        i += 1