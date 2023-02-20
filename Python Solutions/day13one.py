import ast

with open('Python Solutions\day13sampleinput.txt', 'r') as f:
    list_file = f.read().split("\n")

def process_lists(list_1, list_2, pair_index):
    
    print("\n")
    pair_index = 0

    if not len(list_1) and len(list_2):
        pair_index += 1
    else: 
        for i, j in zip(list_1, list_2):
            print (i, j)
            if type(i) == int and type(j) == int:
                if i < j:
                    pair_index += 1
                    break
            if type(i) == list and type(j) == list:
                pair_index = process_lists(i, j, pair_index)
                if len(list_1) < len(list_2):
                    pair_index += 1
                    break
            if type(i) == list and type(j) == int:
                j = [j]
                pair_index = process_lists(i, j, pair_index)
            if type(i) == int and type(j) == list:
                i = [i]
                pair_index = process_lists(i, j, pair_index)

    return pair_index

i = 0
in_order = []
while(i < len(list_file) - 1): 
    
    pair_index = 0
    curr_list_1 = ast.literal_eval(list_file[i])
    curr_list_2 = ast.literal_eval(list_file[i + 1])

    in_order.append(process_lists(curr_list_1, curr_list_2, pair_index))

    i+= 3

sum = 0 
for index, items in enumerate(in_order):
    if items:
        sum += (index + 1)

print(f"\nIndices in order: {in_order}")
print(f"Total sum of right-order indices: {sum}")

