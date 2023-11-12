def adder(tall1: int, tall2: int):
    return tall1 + tall2

def tell_forekomst(text: str, letter: str):
    times_found = 0
    for i in text:
        if i == letter:
            times_found += 1
    return times_found

input_text = input("Skriv inn tekst: ")
input_letter = input("Skriv inn bokstaven: ")
print("Bokstaven", input_letter, "finnes",
      tell_forekomst(input_text, input_letter), 
      "ganger i teksten", input_text)

tall1 = 2
tall2 = 3
tall_sum = adder(tall1, tall2)
print(f'{tall1} + {tall2} = {tall_sum}')

tall1 = 10
tall2 = 66
tall_sum = adder(tall1, tall2)
print(f'{tall1} + {tall2} = {tall_sum}')

