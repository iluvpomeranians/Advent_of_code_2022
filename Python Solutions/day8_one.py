from collections import defaultdict

coordinates = defaultdict(list)

def get_coordinates(numbers_str):
  for y, line in enumerate(numbers_str.split('\n')):
    for x, num in enumerate(line):
      coordinates[(x, y)] = int(num) #tuple key with num as value
  return coordinates


with open('Python Solutions\day8visibletrees.txt', 'r') as f:
  numbers_str = f.read()
  coordinates = get_coordinates(numbers_str)

  max_x = max(coordinates.keys(), key=lambda item: item[0])[0] 
  max_y = max(coordinates.keys(), key=lambda item: item[1])[1]  
  east_bool = False
  west_bool = False
  north_bool = False
  south_bool = False
  count_visible_trees = 0 

  for (x, y), value in coordinates.items():
    
    if(x != 0 and y != 0 and x != max_x and y != max_y):
      #print (f"({x},{y}): {value}")

      alt_x = x
      alt_y = y
      curr_value = value
      east_value = coordinates.get((alt_x+1, alt_y))
      west_value = coordinates.get((alt_x-1, alt_y)) 
      north_value = coordinates.get((alt_x, alt_y-1))       
      south_value = coordinates.get((alt_x, alt_y+1)) 

      #EAST  
      while(east_value is not None and alt_x < max_x): 
        if(curr_value > east_value):
          alt_x += 1
          east_value = coordinates.get((alt_x+1, alt_y))
          east_bool = True
        else:
            east_bool = False
            break
      
      alt_x = x
      alt_y = y

      if east_bool == True:
        #print("Viewable from East")
        count_visible_trees += 1
        continue

      #WEST  
      while(west_value is not None and alt_x > 0): 
        if(curr_value > west_value):
          alt_x -= 1
          west_value = coordinates.get((alt_x-1, alt_y))
          west_bool = True
        else:
            west_bool = False
            break
      
      alt_x = x
      alt_y = y

      if west_bool == True:
        #print("Viewable from West")
        count_visible_trees += 1
        continue

      #NORTH  
      while(north_value is not None and alt_y > 0): 
        if(curr_value > north_value):
          alt_y -= 1
          north_value = coordinates.get((alt_x, alt_y - 1))
          north_bool = True
        else:
            north_bool = False
            break
      
      alt_x = x
      alt_y = y

      if north_bool == True:
        #print("Viewable from North")
        count_visible_trees += 1
        continue
    
      #SOUTH  
      while(south_value is not None and alt_y < max_y): 
        if(curr_value > south_value):
          alt_y += 1
          south_value = coordinates.get((alt_x, alt_y + 1))
          south_bool = True
        else:
            south_bool = False
            break
      
      alt_x = x
      alt_y = y

      if south_bool == True:
        #print("Viewable from South")
        count_visible_trees += 1
        continue
     
    if x == max_x - 1  and y == max_y - 1:
      break


outer_tree_sum = ((max_x + 1) * 2) + ((max_y - 1) * 2)
print (f"\n# of outer trees: {outer_tree_sum}")
print (f"\n# of visible trees from outside the grid: {count_visible_trees}\n")
count_visible_trees += outer_tree_sum
print (f"TOTAL visible trees from outside the grid: {count_visible_trees}\n")
  

 

