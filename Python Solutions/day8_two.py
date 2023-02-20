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
  scenic_scores = []
  east_score = 1
  west_score = 1
  north_score = 1
  south_score = 1   
    

  for (x, y), value in coordinates.items():
    
    score = 0 
    index = x

    if(x != 0 and y != 0 and x != max_x and y != max_y):
      print (f"({x},{y}): {value}") 
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
          east_score = (alt_x - x)
        else:
            east_bool = False
            east_score = (alt_x - x) + 1 
            print (f"East Scenic Score:{east_score}")
            break
      
      alt_x = x
      alt_y = y
        

      #WEST  
      while(west_value is not None and alt_x > 0): 
        if(curr_value > west_value):
          alt_x -= 1
          west_value = coordinates.get((alt_x-1, alt_y))
          west_bool = True
          west_score = (x - alt_x)
        else:
            west_bool = False
            west_score = (x - alt_x) + 1
            print (f"West Scenic Score:{west_score}")
            break
      
      alt_x = x
      alt_y = y
        

      #NORTH  
      while(north_value is not None and alt_y > 0): 
        if(curr_value > north_value):
          alt_y -= 1
          north_value = coordinates.get((alt_x, alt_y - 1))
          north_bool = True
          north_score = (y - alt_y)
        else:
            north_bool = False
            north_score = (y - alt_y) + 1
            print (f"North Scenic Score:{north_score}")
            break
      
      alt_x = x
      alt_y = y
        
    
      #SOUTH  
      while(south_value is not None and alt_y < max_y): 
        if(curr_value > south_value):
          alt_y += 1
          south_value = coordinates.get((alt_x, alt_y + 1))
          south_bool = True
          south_score = (alt_y - y)
        else:
            south_bool = False
            south_score = (alt_y - y) + 1
            print (f"South Scenic Score:{south_score}")
            break
      
      alt_x = x
      alt_y = y
        

    score = (north_score * west_score * south_score * east_score )
    
    print (f"Current Score: {score}\n")     
    
    scenic_scores.append(score)

    if x == max_x - 1  and y == max_y - 1:
      break


highest_score = sorted(scenic_scores, reverse=True)[0]
print("The highest score is: ", highest_score)




 

