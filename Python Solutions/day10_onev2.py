filename = 'Python Solutions\day10_input.txt'

input_list = []
with open(filename, 'r') as file:
    for line in file:
        line_list = line.split()
        if line_list[0] == "addx":
            input_list.append((line_list[0], int(line_list[1])))
        else:
            input_list.append((line_list[0], None))


register_x = 1
total_cycle_count = 0
register_unique_values = set()

for index, line in enumerate(input_list):
    #print(f"{index} {line}\n")
    if line[0] == "noop":
    
        total_cycle_count += 1            
        if(total_cycle_count == 20 or total_cycle_count == 60 or total_cycle_count == 100 or total_cycle_count == 140 or total_cycle_count == 180 or total_cycle_count == 220):
            print(f"Noop value of reg X: {register_x} at Cycle: {total_cycle_count}")
            register_unique_values.add(register_x * total_cycle_count)
    
    elif line[0] == "addx":
        
        total_cycle_count += 1
        if(total_cycle_count == 20 or total_cycle_count == 60 or total_cycle_count == 100 or total_cycle_count == 140 or total_cycle_count == 180 or total_cycle_count == 220):
            print(f"Midcycle value of reg X: {register_x} at Cycle: {total_cycle_count}")
            register_unique_values.add(register_x * total_cycle_count)
        
        total_cycle_count += 1
        if(total_cycle_count == 20 or total_cycle_count == 60 or total_cycle_count == 100 or total_cycle_count == 140 or total_cycle_count == 180 or total_cycle_count == 220):
            print(f"End of 2 cycles for addx, value of reg X: {register_x} at Cycle: {total_cycle_count}")
            register_unique_values.add(register_x * total_cycle_count)
        register_x += line[1]
        

print(f"\n# of cycles: {total_cycle_count} and Register X: {register_x}")

ordered_list = sorted(register_unique_values)

print(f"{ordered_list}")
result = sum(ordered_list)
print(f"Signal strength total sum: {result}")

