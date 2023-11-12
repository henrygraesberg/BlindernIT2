def adder(tall_en: int, tall_to: int):
    return tall_en + tall_to

def tell_forekomst(text: str, letter: str):
    times_found = 0
    for i in text:
        if i == letter:
            times_found += 1
    return times_found

print("{} + {} = {}".format(2, 5, adder(2, 5)))
print("{} + {} = {} \n".format(7, 101, adder(7, 101)))

input_text = input("Skriv inn tekst: ")
input_letter = input("Skriv inn bokstaven: ")
print("Bokstaven", input_letter, "finnes",
      tell_forekomst(input_text, input_letter), 
      "ganger i teksten", input_text)