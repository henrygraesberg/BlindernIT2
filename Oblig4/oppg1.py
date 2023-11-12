def product_list(list: list):
    product = list[0]
    for i in range(1, len(list)):
        product *= list[i]
    
    return product

tall_list = [0, 5, 10]
tall_list.append(12)
print(tall_list[0], tall_list[2])
navn_list = []

for i in range(4):
    user_in = input("Skriv et navn: ")

    navn_list.append(user_in)

if "Henry" in navn_list or "henry" in navn_list:
    print("Du husket med!")
else:
    print("Glemte du meg?")

sum_produkt = [sum(tall_list), product_list(tall_list)]
print(sum_produkt)
#Oppgaven kan tolkes på to måter, enten å sette begge listene i en ny
#list, som gjort her
new_list = [tall_list, sum_produkt]
print(new_list)

new_list.pop()
new_list.pop()
print(new_list)

#Eller å slå sammen verdiene fra begge listene
new_list = []
for i in tall_list:
    new_list.append(i)
for i in sum_produkt:
    new_list.append(i)

print(new_list)

new_list.pop()
new_list.pop()
print(new_list)
