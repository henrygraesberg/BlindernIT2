def tallTilListe(num: int):
    num_list = []
    numstr = str(num)

    for i in range(len(numstr)):
        num_list.append(int(numstr[i]))
    
    return num_list