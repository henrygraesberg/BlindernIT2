vare_dict = {
    "melk": 14.90,
    "brød": 24.90,
    "yoghurt": 12.90,
    "pizza": 39.90
}

print(vare_dict)

def append_product(dictionary: dict):
    user_in = {
        "product": input("Skriv et varenavn: "),
        "price": int(input("Skriv en pris i kr: "))
    }

    dictionary[user_in["product"]] = user_in["price"]

for i in range(2):
    append_product(vare_dict)

print(vare_dict)
