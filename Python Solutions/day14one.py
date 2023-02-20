from collections import defaultdict

with open('Python Solutions\day14input.txt', 'r') as f: 
    list_file = f.read().strip().split("\n")

corners = []
coordinates = defaultdict(set)
for top_index, lines in enumerate(list_file):
    corners.append(lines.split('->'))
    for index, coordinate in enumerate(corners[top_index]):
        (x,y) = map(int, coordinate.replace('(', '').replace(')', '').strip().split(','))
        if index + 1 < len(corners[top_index]):
            next_coordinate = corners[top_index][index + 1]
            (x_2, y_2) = map(int, next_coordinate.replace('(', '').replace(')', '').strip().split(','))
            if x == x_2:
                if y - y_2 < 0:
                    i = 0
                    while(i < abs(y - y_2)):
                        y += 1
                        corners[top_index].insert(index + 1, f"{x},{y}".strip())
                        i += 1
                elif y - y_2 > 0:
                    i = 0
                    while(i < abs(y - y_2)):
                        y -= 1
                        corners[top_index].insert(index + 1, f"{x},{y}".strip())
                        i += 1
            elif y == y_2:
                if x - x_2 < 0:
                    i = 0
                    while(i < abs(x - x_2)):
                        x += 1
                        corners[top_index].insert(index + 1, f"{x},{y}".strip())
                        i += 1
                elif x - x_2 > 0:
                    i = 0
                    while(i < abs(x - x_2)):
                        x -= 1
                        corners[top_index].insert(index + 1, f"{x},{y}".strip())
                        i += 1

for i,sublist in enumerate(corners):
    sublist = [c.strip() for c in sublist]
    sublist = set(sublist)
    for rock in sublist:
        coordinates[rock] = '#' 
coordinates[f"{500},{0}"] = '+'

sorted_X_coordinates = sorted(coordinates, key=lambda x: int(x.split(',')[0]))
sorted_Y_coordinates = sorted(coordinates, key=lambda x: int(x.split(',')[1]))

min_x = int(sorted_X_coordinates[0].split(',')[0])
max_x = int(sorted_X_coordinates[len(sorted_X_coordinates) - 1].split(',')[0])
min_y = int(sorted_Y_coordinates[0].split(',')[1])
max_y = int(sorted_Y_coordinates[len(sorted_Y_coordinates) - 1].split(',')[1])
print(min_x, max_x, min_y, max_y)

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        coord = f"{x},{y}"
        if coord is not coordinates and coordinates[coord] != '#' and coordinates[coord] != 'o' and coordinates[coord] != '+':
            coordinates[coord] = "."

x = 500
y = 1
count = 0
while (coordinates[f"{x},{y}"] == '.'):
    down_y = y + 1
    left_x = x - 1
    right_x = x + 1
    count += 1
    if coordinates[f"{x},{down_y}"] == 'o' or coordinates[f"{x},{down_y}"] == '#':
        if coordinates[f"{left_x},{down_y}"] == 'o' or coordinates[f"{left_x},{down_y}"] == '#':
            if coordinates[f"{right_x},{down_y}"] == 'o' or coordinates[f"{right_x},{down_y}"] == '#':
                coordinates[f"{x},{y}"] = 'o'
                x = 500
                y = 1 
                continue
            else: 
                x = right_x
                y = down_y
                continue
        else: 
            x = left_x
            y = down_y
            continue
           
    y += 1

sand_count = 0
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        coord = f"{x},{y}"
        if coord in coordinates and coordinates[coord] == '#':
            print("#", end="")
        elif coord in coordinates and coordinates[coord] == '+':
            print("+", end="")
        elif coord in coordinates and coordinates[coord] == 'o':
            sand_count += 1
            print("O", end="")
        else:
            print(".", end="")
    print("")


print(f"Total units of sand resting: {sand_count}")








    



