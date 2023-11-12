def find_min(list):
    smallest_value = list[0]
    
    for i in range(1, len(list)):
        index_val = list[i]
        
        if index_val < smallest_value:
            smallest_value = index_val

    return smallest_value

def find_max(list):
    largest_value = list[0]
    
    for i in range(1, len(list)):
        index_val = list[i]
        
        if index_val > largest_value:
            largest_value = index_val

    return largest_value

def linebreak():
    print("\n")

input_value = None
tall = []
while input_value != 0:
    input_value = int(input("skriv inn et tall: "))
    tall.append(input_value)

linebreak()

for i in range(len(tall)):
    print(f'{i}:  {tall[i]}')

linebreak()

min_sum = 0
for i in range(len(tall)):
    min_sum += tall[i]

print(f'Summen: {min_sum}')

linebreak()

print(f'Lavest tall: {find_min(tall)}',
      f'Høyest tall: {find_max(tall)}', sep="\n")