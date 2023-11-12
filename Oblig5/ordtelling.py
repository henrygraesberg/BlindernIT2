def antall_bokstaver(ord: str):
    return len(ord)

def antall_ord(setning: str):
    setning_list = setning.split()
    
    setning_dict = {}

    for word in setning_list:
        if word not in setning_dict:
            setning_dict[word] = 1
        else:
            setning_dict[word] += 1
    
    return setning_dict

def unique_words(setning: str):
    setning_list = setning.split()
    
    setning_new_list = []

    for word in setning_list:
        if word not in setning_new_list:
            setning_new_list.append(word)
    
    return setning_new_list

user_setning = input("Skriv en setning: ")
ord_i_setningen = antall_ord(user_setning)

print(f'antall ord i setningen din er {len(user_setning.split())}')
print(ord_i_setningen)

unique = unique_words(user_setning)
for i in unique:
    print(f'{i} består av {antall_bokstaver(i)} bokstaver')