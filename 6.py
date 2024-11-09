item_l = 9
item_list = []
while len(item_list) < item_l:
    items = input("enter number: ")
    new_list = item_list.append(items)

    output1 = item_list
    output2 = tuple(item_list)
    print(f'List: ', output1)
    print(f'Tuple: ', output2)
