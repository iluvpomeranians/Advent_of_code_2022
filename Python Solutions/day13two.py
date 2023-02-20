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

    if process_lists(curr_list_1, curr_list_2) == 1: 
        in_order.append(curr_list_1)
        in_order.append(curr_list_2)
    else:
        in_order.append(curr_list_2)
        in_order.append(curr_list_1)


    i+= 3

sum = 0 
for index, items in enumerate(in_order):
    if items:
        sum += (index + 1)

in_order.extend([ast.literal_eval("[[2]]"), ast.literal_eval("[[6]]")])

def quickSort(in_order, low, high):
    if low < high:
        pi = partition(in_order, low, high)
        quickSort(in_order, low, pi-1)
        quickSort(in_order, pi+1, high)

def partition(in_order, low, high):
    pivot = in_order[high]
    i = low - 1
    for j in range(low, high):
        if process_lists(in_order[j], pivot) == 1:
            i = i + 1
            in_order[i], in_order[j] = in_order[j], in_order[i]
    in_order[i + 1], in_order[high] = in_order[high], in_order[i + 1]
    return i + 1

decoder_key = 1
n = len(in_order)
quickSort(in_order, 0, n-1)
for index,lists in enumerate(in_order):
    if lists == ast.literal_eval("[[2]]") or lists == ast.literal_eval("[[6]]"):
        decoder_key *= (index + 1)
        print(f"{lists} at index: {index + 1}")

print(f"Decoder Key = {decoder_key}")








## Start = min##
## if start < start[i+1]
#   start 