from collections import defaultdict, deque
import time

#Timing: Star
start = time.perf_counter()

filename = 'Python Solutions\day11input.txt'

input_list_dict = {}
with open(filename, 'r') as file:
    monkey_num = None
    for line in file:
        line = line.rstrip()
        if line.startswith("Monkey"):
            monkey_num = line.split(':')[0].split(' ')[1]
            input_list_dict[monkey_num] = []
        else:
            input_list_dict[monkey_num].append(line.strip())

old = None
monkey_queues = defaultdict(deque)
monkey_activity = defaultdict(int)
round_number = 0
mod_all = 1

#Find common multiple of all monkeys' divisors 
for monkey_num, data in input_list_dict.items():
    for lines in data: 
        if lines.startswith("Test"):
            test = lines.split(':')[1].split('by')[1]
            test = int(test.strip())
            mod_all *= test

while (round_number < 10000):

    for monkey_num, data in input_list_dict.items():
        
        operation = None
        test = None
        true_next = None
        false_next = None
        number_list = None
        new = None
        count = 0

        for lines in data:
            if lines.startswith("Starting") and round_number + 1 == 1:
                monkey_queues[monkey_num].extend([int(x) for x in lines.split(':')[1].split(',')])
            if lines.startswith("Operation"):
                operation = lines.split(':')[1].split('=')[1]
                operation = operation.strip()
            if lines.startswith("Test"):
                test = lines.split(':')[1].split('by')[1]
                test = int(test.strip())
            if lines.startswith("If true"):
                true_next = lines.split(':')[1].split('monkey')[1]
                true_next = true_next.strip()
            if lines.startswith("If false"):
                false_next = lines.split(':')[1].split('monkey')[1]
                false_next = false_next.strip()
        
        if operation is not None and test is not None and true_next is not None and false_next is not None: 
            
            while monkey_queues[monkey_num]:
                
                old = monkey_queues[monkey_num].popleft()
                result = eval(operation)  
                new = result % mod_all

                if new % test == 0:
                    monkey_queues[true_next].append(new)
                else:
                    monkey_queues[false_next].append(new)
                
                count += 1
                       
            monkey_activity[monkey_num] += count

    round_number += 1


#for monkey_num, data in monkey_activity.items():
#    print(f"Monkey {monkey_num} inspected items {data} times.")

sorted_activity = sorted(monkey_activity.items(), key=lambda x: x[1], reverse=True)
top_two = sorted_activity[:2]
result = top_two[0][1] * top_two[1][1]
print(f"The top two monkeys inspected items {top_two[0][1]} and {top_two[1][1]} times respectively, the amount of monkey buisness: {result}")

#Timing: End
end = time.perf_counter()
print(f"\nTime to complete = {(end-start)*1000:.2f} milliseconds.")