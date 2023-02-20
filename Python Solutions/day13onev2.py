import ast
from itertools import zip_longest

with open('Python Solutions\day13input.txt', 'r') as f:
    list_file = f.read().strip().split("\n")

def process_lists(list_1, list_2):
    
    for index, (i, j) in enumerate(zip_longest(list_1, list_2)):
        if (index >= len(list_1)):
            return 1
        if (index >= len(list_2)):
            return 0
        pair_index = -1
        if type(i) == int and type(j) == int:
            if i < j:
                pair_index = 1
            elif i > j:
                pair_index = 0
            else:
                pair_index = -1
                continue
        elif type(i) == list and type(j) == list:
            pair_index = process_lists(i, j)
        elif type(i) == list and type(j) == int:
            pair_index = process_lists(i, [j])
        elif type(i) == int and type(j) == list:
            pair_index = process_lists([i], j)
        if pair_index != -1:
            return pair_index
    return -1 

i = 0
in_order = []
while(i < len(list_file) - 1): 

    curr_list_1 = ast.literal_eval(list_file[i])
    curr_list_2 = ast.literal_eval(list_file[i + 1])

    in_order.append(process_lists(curr_list_1, curr_list_2))

    i+= 3

sum = 0 
for index, items in enumerate(in_order):
    if items:
        sum += (index + 1)

print(f"Total sum of in-order indices: {sum}")

