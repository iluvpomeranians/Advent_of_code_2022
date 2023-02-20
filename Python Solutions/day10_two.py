filename = 'Python Solutions\day10_input.txt'

input_list = []
with open(filename, 'r') as file:
    for line in file:
        line_list = line.split()
        if line_list[0] == "addx":
            input_list.append((line_list[0], int(line_list[1])))
        else:
            input_list.append((line_list[0], None))

sprite_pos = ['#', '#', '#', '.', '.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
CRT_list = [[]]
register_x = 1
total_cycle_count = 0

def CRT_draw(crt_cycle_count: int, sprite: list[str], CRT_list: list[list[str]]): 
    if sprite[crt_cycle_count - 1] == '#':
        CRT_list[-1].append("#")
    else:
        CRT_list[-1].append(".")
    if len(CRT_list[-1]) == 40:
        crt_cycle_count = 0
        CRT_list.append([])

    return crt_cycle_count
        
 
def Update_Sprite(register: int, sprite: list[str]):
    alt_sprite = ['.'] * 40
    for character in sprite:
        if character == '#':
            character = '.'
    
    if 0 <= register < len(alt_sprite):
        alt_sprite[register] = '#'

    
    if 0 <= register-1 < len(alt_sprite):
        alt_sprite[register-1] = '#'


    if 0 <= register+1 < len(alt_sprite):
        alt_sprite[register+1] = '#'

    
    return alt_sprite


for index, line in enumerate(input_list):

    if line[0] == "noop":
    
        total_cycle_count += 1            
        total_cycle_count = CRT_draw(total_cycle_count, sprite_pos, CRT_list)
    
    elif line[0] == "addx":
        
        total_cycle_count += 1
        total_cycle_count = CRT_draw(total_cycle_count, sprite_pos, CRT_list) 
        total_cycle_count += 1
        register_x += int(line[1])
        total_cycle_count = CRT_draw(total_cycle_count, sprite_pos, CRT_list)
        sprite_pos = Update_Sprite(register_x, sprite_pos)

for i in range(len(CRT_list)):
    print(''.join(CRT_list[i]))




