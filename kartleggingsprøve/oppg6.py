def spoer_is():
    user_in = int(input("Hvor mange kuler is vil du ha? "))
    price = user_in * 30
    return f'Det koster {price}kr'

def spoer_pizza():
    user_in = input("Hva vil du ha på pizzaen din? ")

    if user_in == "ost":
        return "En ostepizza koster 80kr"
    
    return f'En pizza med {user_in} på koster 100kr'

def spoer_spise():
    user_in = input("Hva skal du ha? ")

    if user_in == "is":
        print(spoer_is())
    elif user_in == "pizza":
        print(spoer_pizza())
    else:
        print("Vi selger ikke det")
        spoer_spise()

spoer_spise()