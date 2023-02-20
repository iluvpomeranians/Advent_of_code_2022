from collections import defaultdict
import re
import heapq

def unique_nodes(string):
    unique_counter = 0
    graph = defaultdict(list)
    rows = [list(row) for row in string.split("\n")]
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            
            node = rows[i][j]

            if node in graph:
                unique_counter += 1
                new_node = node + "_" + str(unique_counter)
                rows[i][j] = new_node
                graph[new_node] = []
            else:
                graph[node] = []

    return rows, graph

def create_graph(list_rows, graph_input):
    graph = graph_input
    rows = list_rows
    for i in range(len(rows)):
        for j in range(len(rows[i])):

            #CURRENT NODE

            node = rows[i][j]

            #NEIGHBORS LETTER EXTRACTION
            if j > 0:
                left = rows[i][j-1]
                left_node_letter = next(re.finditer(r'\w', left)).group()
                if left == 'S':
                    left_node_val = ord('a') 
                elif left == 'E':
                    left_node_val = ord('z')
                else:
                    left_node_val = ord(left_node_letter) 
            if j < len(rows[i]) - 1:
                right = rows[i][j+1]
                right_node_letter = next(re.finditer(r'\w', right)).group()
                if right == 'S':
                    right_node_val = ord('a') 
                elif right == 'E':
                    right_node_val = ord('z')
                else:
                    right_node_val = ord(right_node_letter)
            if i < len(rows) - 1:
                down = rows[i+1][j]
                down_node_letter = next(re.finditer(r'\w', down)).group()
                if down == 'S':
                    down_node_val = ord('a') 
                elif down == 'E':
                    down_node_val = ord('z')
                else:
                    down_node_val = ord(down_node_letter)
            if i > 0:
                up = rows[i-1][j]
                up_node_letter = next(re.finditer(r'\w', up)).group()
                if up == 'S':
                    up_node_val = ord('a') 
                elif up == 'E':
                    up_node_val = ord('z')
                else:
                    up_node_val = ord(up_node_letter)
            
            if node == 'S':
                current_node_val = ord('a') 
            elif node == 'E':
                current_node_val = ord('z')  
            else: 
                current_node_val = ord(next(re.finditer(r'\w', node)).group())

            
            #LEFT-CHECK
            if j > 0 and left_node_val - current_node_val in [0,1]: 
                graph[node].append(rows[i][j-1]) 
            if j > 0 and current_node_val - left_node_val >= 1:
                graph[node].append(rows[i][j-1])  

            #RIGHT-CHECK
            if j < len(rows[i]) - 1 and right_node_val - current_node_val in [0,1]:
                graph[node].append(rows[i][j+1])  
            if j < len(rows[i]) - 1 and current_node_val- right_node_val >= 1:
                graph[node].append(rows[i][j+1])  

            #UP-CHECK
            if i > 0 and up_node_val - current_node_val in [0,1]:
                graph[node].append(rows[i-1][j])   
            if i > 0 and current_node_val - up_node_val >= 1:
                graph[node].append(rows[i-1][j])  

            #DOWN-CHECK
            if i < len(rows) - 1 and down_node_val - current_node_val in [0,1]:
                graph[node].append(rows[i+1][j])  
            if i < len(rows) - 1 and current_node_val- down_node_val >= 1:
                graph[node].append(rows[i+1][j])    

                 
    return graph


def find_shortest_path(graph, start, end):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return cost
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost + 1, neighbor))
    return float('inf')


filename = 'Python Solutions\day12input.txt'

with open(filename, 'r') as f:
    string = f.read()
    rows, graph = unique_nodes(string)
    updated_graph = create_graph(rows, graph)
    shortest_path_length = find_shortest_path(updated_graph, 'S', 'E')
    print(f"Size: {shortest_path_length}")









