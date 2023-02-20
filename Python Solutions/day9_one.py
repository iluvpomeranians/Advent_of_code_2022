from collections import defaultdict

positions = defaultdict(lambda: (0, 0))
positions["H"]      = (0, 0)
positions["T"]      = (0, 0)
positions["s"]      = (0, 0)
tail_visits = []

tail_visits.append((0, 0))

with open('Python Solutions\day9input.txt', 'r') as f:
  directives = f.readlines()
  
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
    
    # Get current coordinates of H & T
    h_x, h_y = positions["H"]
    t_x, t_y = positions["T"]

    #Store in alternate variables to protect current vales of (x,y)
    h_alt_x = h_x
    h_alt_y = h_y
    t_alt_x = t_x
    t_alt_y = t_y

    ###########################
    #CURRENT RELATIVE POSITIONS
    ###########################

    #overlapping
    if(h_y == t_y and h_x == t_x):
        overlapping      = True
    
    #horizontally sidebyside
    if(h_y == t_y):  
        if(h_x < t_x):
            left_adj     = True
        if(h_x > t_x):
            right_adj    = True

    #vertically sidebyside
    if(h_x == t_x):  
        if(h_y < t_y):
            bottom_adj   = True
        if(h_y > t_y):
            top_adj      = True

    #top-right diagonal
    if(h_x == t_x + 1 and h_y == t_y + 1): 
        diag_top_right   = True

    #bottom-left diagonal
    if(h_x == t_x - 1 and h_y == t_y - 1): 
        diag_bottom_left = True

    #top-left diagonal  
    if(h_x == t_x - 1 and h_y == t_y + 1): 
        diag_top_left    = True
    
    #bottom-right diagonal
    if(h_x == t_x + 1 and h_y == t_y - 1): 
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
            if(count >= 2):
                h_x_temp = h_x
                h_x_temp += 1
                while(h_x_temp < h_alt_x):
                    tail_visits.append((h_x_temp, h_y))
                    h_x_temp += 1
        if(diag_bottom_left or diag_top_left or left_adj):
            if(count > 2):
                h_x_temp = h_x
                h_x_temp += 2
                while(h_x_temp < h_alt_x):
                    tail_visits.append((h_x_temp, h_y))
                    h_x_temp += 1  
        if(right_adj or diag_bottom_right or diag_top_right):
            while(h_x < h_alt_x):
                tail_visits.append((h_x, h_y))
                h_x += 1

    elif direction == "L":
        h_alt_x -= count
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
        if(overlapping or bottom_adj or top_adj):
            if(count >= 2):
                h_x_temp = h_x
                h_x_temp -= 1
                while(h_x_temp > h_alt_x):
                    tail_visits.append((h_x_temp, h_y))
                    h_x_temp -= 1
        if(diag_bottom_right or diag_top_right or right_adj):
            if(count > 2):
                h_x_temp = h_x
                h_x_temp -= 2
                while(h_x_temp > h_alt_x):
                    tail_visits.append((h_x_temp, h_y))
                    h_x_temp -= 1
        if(left_adj or diag_bottom_left or diag_top_left):
            while(h_x > h_alt_x):
                tail_visits.append((h_x, h_y))
                h_x -= 1

    
    elif direction == "U":
        h_alt_y += count
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
            if(count >= 2):
                h_y_temp = h_y
                h_y_temp += 1
                while(h_y_temp < h_alt_y):
                    tail_visits.append((h_x, h_y_temp))
                    h_y_temp += 1
        if(diag_bottom_left or diag_bottom_right or bottom_adj):
            if (count > 2):
                h_y_temp = h_y
                h_y_temp += 2
                while(h_y_temp < h_alt_y):
                    tail_visits.append((h_x, h_y_temp))
                    h_y_temp += 1
        if(top_adj or diag_top_left or diag_top_right):
            while(h_y < h_alt_y):
                tail_visits.append((h_x, h_y))
                h_y += 1


    elif direction == "D":
        h_alt_y -= count
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
            if(count >= 2):
                h_y_temp = h_y
                h_y_temp -= 1
                while(h_y_temp > h_alt_y):
                    tail_visits.append((h_x, h_y_temp))
                    h_y_temp -= 1
        if(top_adj or diag_top_right or diag_top_left):
            if(count > 2):
                h_y_temp = h_y
                h_y_temp -= 2
                while(h_y_temp > h_alt_y):
                    tail_visits.append((h_x, h_y_temp))
                    h_y_temp -= 1
        if(bottom_adj or diag_bottom_right or diag_bottom_left):
            while(h_y > h_alt_y):
                tail_visits.append((h_x, h_y))
                h_y -= 1
                 
    h_x = h_alt_x
    h_y = h_alt_y
    t_x = t_alt_x
    t_y = t_alt_y

    positions["H"] = (h_x, h_y)
    positions["T"] = (t_x, t_y)
    tail_visits.append((t_x, t_y))
   
#print(f"H: {positions['H']} T: {positions['T']}")

unique_combinations = set(tail_visits)
#print([visit for visit in tail_visits])
num_unique_combinations = len(unique_combinations)
print(f"# of tail visits (at least one time each): {num_unique_combinations}")
