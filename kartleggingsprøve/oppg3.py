def add_to_list(num_list: "list[int]", add_num: int):
    new_list = []

    for i in num_list:
        new_list.append(i + add_num)
    
    return new_list