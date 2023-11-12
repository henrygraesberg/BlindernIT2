stop = False

while stop is not True:
    user_in = float(input("Skriv et tall"))
    if user_in >= 10:
        stop = True
    else:
        print("igjen!")