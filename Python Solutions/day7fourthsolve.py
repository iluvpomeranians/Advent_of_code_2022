from collections import defaultdict

with open("Python Solutions\day7puzzleinput.txt") as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []

for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):
        continue
    if c.startswith("$ cd"):
        dest = c.split()[2]
        if dest == "..":
            stack.pop()
        else:
            path = f"{stack[-1]}/{dest}" if stack else dest
            stack.append(path)
    else:
        file_size = c.split()[0]
        for path in stack: 
            sizes[path] += int(file_size)

print (sum(n for n in sizes.values() if n <= 100000)) 
