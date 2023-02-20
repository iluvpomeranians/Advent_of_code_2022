from collections import defaultdict

positions = defaultdict(lambda: (0, 0))
positions["H"]      = (0, 0)
positions["1"]      = (0, 0)
positions["2"]      = (0, 0)
positions["3"]      = (0, 0)
positions["4"]      = (0, 0)
positions["5"]      = (0, 0)
positions["6"]      = (0, 0)
positions["8"]      = (0, 0)
positions["8"]      = (0, 0)
positions["9"]      = (0, 0)
positions["s"]      = (0, 0)
tail_visits = []


# def update_coordinates(positions, curr_head_x, curr_tail_y):
#     prev_key, prev_value = None, None
#     for key, value in positions.items():
#         if prev_key is not None:
#             print(f"Previous key: {prev_key}, value: {prev_value}")
#             new_x = value[0] + curr_head_x
#             new_y = value[1] + curr_tail_y
#             positions[prev_key] = (new_x, new_y)
#         print(f"Current key: {key}, value: {value}")
#         prev_key, prev_value = key, value


tail_visits.append((0, 0))

with open('Python Solutions\day9_two_inputtext.txt', 'r') as f:
  directives = f.readlines()

tail_keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  
for d in directives: 
    direction, count = d.split()
    count = int(count)
    #print(f"Move {direction} by {count}")
 
    overlapping         = False
    right_adj           = False
    left_adj            = False
    top_adj             = False
    bottom_adj          = False
    diag_top_right      = False
    diag_top_left       = False
    diag_bottom_right   = False
    diag_bottom_left    = False

    prev_key = "H"
    
    for curr_key in tail_keys:
        curr_value = positions[curr_key]
        prev_value = positions[prev_key]
    
        #Store in alternate variables to protect current vales of (x,y)
        h_alt_x = prev_value[0]
        h_alt_y = prev_value[1]
        t_alt_x = curr_value[0]
        t_alt_y = curr_value[1]


        ###########################
        #CURRENT RELATIVE POSITIONS
        ###########################

        #overlapping
        if(prev_value[1] == curr_value[1] and prev_value[0] == curr_value[0]):
            overlapping      = True
        
        #horizontally sidebyside
        if(prev_value[1] == curr_value[1]):  
            if(prev_value[0] < curr_value[0]):
                left_adj     = True
            if(prev_value[0] > curr_value[0]):
                right_adj    = True

        #vertically sidebyside
        if(prev_value[0] == curr_value[0]):  
            if(prev_value[1] < curr_value[1]):
                bottom_adj   = True
            if(prev_value[1] > curr_value[1]):
                top_adj      = True

        #top-right diagonal
        if(prev_value[0] == curr_value[0] + 1 and prev_value[1] == curr_value[1] + 1): 
            diag_top_right   = True

        #bottom-left diagonal
        if(prev_value[0] == curr_value[0] - 1 and prev_value[1] == curr_value[1] - 1): 
            diag_bottom_left = True

        #top-left diagonal  
        if(prev_value[0] == curr_value[0] - 1 and prev_value[1] == curr_value[1] + 1): 
            diag_top_left    = True
        
        #bottom-right diagonal
        if(prev_value[0] == curr_value[0] + 1 and prev_value[1] == curr_value[1] - 1): 
            diag_bottom_right  = True

        ##################################
        ##### UPDATING COORDINATES #######
        ##################################
        
        if direction == "R":
            
            h_alt_x += count
            if(bottom_adj or top_adj or left_adj or overlapping):
                if(count >= 2):
                    t_alt_x = h_alt_x - 1
                    t_alt_y = h_alt_y
            if(diag_top_left or diag_bottom_left):
                if(count > 2):
                    t_alt_x = h_alt_x - 1
                    t_alt_y = h_alt_y
            if(right_adj or diag_top_right or diag_bottom_right):
                t_alt_y = h_alt_y
                t_alt_x = h_alt_x - 1
            if(overlapping or bottom_adj or top_adj):
                if(curr_key == "9"):
                    if(count >= 2):
                        h_x_temp = prev_value[0]
                        h_x_temp += 1
                        while(h_x_temp < h_alt_x):
                            tail_visits.append((h_x_temp, prev_value[1]))
                            h_x_temp += 1
            if(diag_bottom_left or diag_top_left or left_adj):
                if(curr_key == "9"):
                    if(count > 2):
                        h_x_temp = prev_value[0]
                        h_x_temp += 2
                        while(h_x_temp < h_alt_x):
                            tail_visits.append((h_x_temp, prev_value[1]))
                            h_x_temp += 1  
            if(right_adj or diag_bottom_right or diag_top_right):
                if(curr_key == "9"):
                    h_x = prev_value[0]
                    while(h_x < h_alt_x):
                        tail_visits.append((h_x, prev_value[1]))
                        h_x += 1

        elif direction == "L":
            
            h_alt_x += count
            if(right_adj or overlapping or bottom_adj or top_adj):
                if(count >= 2):
                    t_alt_y = h_alt_y
                    t_alt_x = h_alt_x + 1
            if(diag_bottom_right or diag_top_right):
                if(count > 2):
                    t_alt_y = h_alt_y
                    t_alt_x = h_alt_x + 1
            if(left_adj or diag_top_left or diag_bottom_left):
                t_alt_y = h_alt_y
                t_alt_x = h_alt_x + 1
            if(overlapping or bottom_adj or top_adj and curr_key == "9"):
                if(count >= 2):
                    h_x_temp = prev_value[0]
                    h_x_temp -= 1
                    while(h_x_temp > h_alt_x):
                        tail_visits.append((h_x_temp, prev_value[1]))
                        h_x_temp -= 1
            if(diag_bottom_right or diag_top_right or right_adj):
                if(curr_key == "9"):
                    if(count > 2):
                        h_x_temp = prev_value[0]
                        h_x_temp -= 2
                        while(h_x_temp > h_alt_x):
                            tail_visits.append((h_x_temp, prev_value[1]))
                            h_x_temp -= 1
            if(left_adj or diag_bottom_left or diag_top_left and curr_key == "9"):
                if(curr_key == "9"):
                    h_x = prev_value[0]
                    while(h_x > h_alt_x):
                        tail_visits.append((h_x, prev_value[1]))
                        h_x -= 1

        
        elif direction == "U":
            
            h_alt_x += count
            if(right_adj or overlapping or left_adj or bottom_adj):
                if(count >= 2):
                    t_alt_x = h_alt_x
                    t_alt_y = h_alt_y - 1
            if(diag_bottom_left or diag_bottom_right):
                if (count > 2):
                    t_alt_x = h_alt_x
                    t_alt_y = h_alt_y - 1
            if(top_adj or diag_top_left or diag_top_right):
                t_alt_x = h_alt_x
                t_alt_y = h_alt_y - 1
            if(overlapping or left_adj or right_adj):
                if(curr_key == "9"):
                    if(count >= 2):
                        h_y_temp = prev_value[1]
                        h_y_temp += 1
                        while(h_y_temp < h_alt_y):
                            tail_visits.append((prev_value[0], h_y_temp))
                            h_y_temp += 1
            if(diag_bottom_left or diag_bottom_right or bottom_adj):
                if(curr_key == "9"):
                    if (count > 2):
                        h_y_temp = prev_value[1]
                        h_y_temp += 2
                        while(h_y_temp < h_alt_y):
                            tail_visits.append((prev_value[0], h_y_temp))
                            h_y_temp += 1
            if(top_adj or diag_top_left or diag_top_right):
                if(curr_key == "9"):
                    h_y = prev_value[1]
                    while(h_y < h_alt_y):
                        tail_visits.append((h_y, prev_value[1]))
                        h_y += 1


        elif direction == "D":
            h_alt_x += count
            if(right_adj or left_adj or overlapping or top_adj):
                if(count >= 2):
                    t_alt_x = h_alt_x
                    t_alt_y = h_alt_y + 1
            if(diag_top_left or diag_top_right):
                if(count > 2):
                    t_alt_x = h_alt_x
                    t_alt_y = h_alt_y + 1
            if(bottom_adj or diag_bottom_left or diag_bottom_right):
                t_alt_x = h_alt_x
                t_alt_y = h_alt_y + 1
            if(right_adj or left_adj or overlapping):
                if(curr_key == "9"):
                    if(count >= 2):
                        h_y_temp = prev_value[1]
                        h_y_temp -= 1
                        while(h_y_temp > h_alt_y):
                            tail_visits.append((prev_value[0], h_y_temp))
                            h_y_temp -= 1
            if(top_adj or diag_top_right or diag_top_left):
                if(curr_key == "9"):
                    if(count > 2):
                        h_y_temp = prev_value[1]
                        h_y_temp -= 2
                        while(h_y_temp > h_alt_y):
                            tail_visits.append((prev_value[0], h_y_temp))
                            h_y_temp -= 1
            if(bottom_adj or diag_bottom_right or diag_bottom_left):
                if(curr_key == "9"):
                    h_y = prev_value[1]
                    while(h_y > h_alt_y):
                        tail_visits.append((h_y, prev_value[1]))
                        h_y -= 1

        #WE need to reassign count and direction by the x-y change in current val
        count = abs(t_alt_x - curr_value[0]) if (curr_value[0] - t_alt_x) != 0 else abs(t_alt_y - curr_value[1])

        if ((t_alt_x - curr_value[0] > 0) and (t_alt_y - curr_value[1] == 0)):
            direction = "R"
        elif((t_alt_x - curr_value[0] < 0) and (t_alt_y - curr_value[1] == 0)):
            direction = "L"
        elif((t_alt_y - curr_value[1] > 0) and (t_alt_x - curr_value[0] == 0)):
            direction = "U"
        elif((t_alt_y - curr_value[1] < 0) and (t_alt_x - curr_value[0] == 0)):
            direction = "D"
        elif((t_alt_y - curr_value[1] != 0) and (t_alt_x - curr_value[0] == 0)):
            direction = "DL"
        
        positions[prev_key] = (h_alt_x, h_alt_y)
        positions[curr_key] = (t_alt_x, t_alt_y)
        if(curr_key == "9"):
            tail_visits.append((t_alt_x, t_alt_y))
   
        
#print(f"H: {positions['H']} T: {positions['T']}")

unique_combinations = set(tail_visits)
print([visit for visit in tail_visits])
num_unique_combinations = len(unique_combinations)
print(f"# of tail visits (at least one time each): {num_unique_combinations}")
