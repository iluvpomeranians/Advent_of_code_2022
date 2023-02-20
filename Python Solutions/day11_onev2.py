from collections import defaultdict, deque

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

while (round_number < 20):

    for monkey_num, data in input_list_dict.items():
        
        print("Monkey :", monkey_num)
        operation = None
        test = None
        true_next = None
        false_next = None
        number_list = None
        new = None

        for lines in data:
            if lines.startswith("Starting") and round_number + 1 == 1:
                monkey_queues[monkey_num].extend([int(x) for x in lines.split(':')[1].split(',')])
            if lines.startswith("Operation"):
                operation = lines.split(':')[1].split('=')[1]
                operation = operation.strip()
                #print(operation)
            if lines.startswith("Test"):
                test = lines.split(':')[1].split('by')[1]
                test = int(test.strip())
                #print(test)
            if lines.startswith("If true"):
                true_next = lines.split(':')[1].split('monkey')[1]
                true_next = true_next.strip()
                #print(true_next)
            if lines.startswith("If false"):
                false_next = lines.split(':')[1].split('monkey')[1]
                false_next = false_next.strip()
                #print(false_next)
        
        if operation is not None and test is not None and true_next is not None and false_next is not None:
            count = 0
            while monkey_queues[monkey_num]:
                num = monkey_queues[monkey_num].popleft()
                old = num 
                result = int((eval(operation))/3)  
                new = int(result)
                
                if new % test == 0:
                    monkey_queues[true_next].append(new)
                    print(f"{new} appended to {true_next}")
                else:
                    monkey_queues[false_next].append(new)
                    print(f"{new} appended to {false_next}")
                count += 1
                
            
            monkey_activity[monkey_num] += count

    print(f"\nROUND # {round_number + 1}\n")                

    for monkey_num, data in monkey_queues.items():
        print(f"Monkey #{monkey_num}: {data}")

    print("\n")
    round_number += 1


for monkey_num, data in monkey_activity.items():
    print(f"Monkey {monkey_num} inspected items {data} times.")

sorted_activity = sorted(monkey_activity.items(), key=lambda x: x[1], reverse=True)
top_two = sorted_activity[:2]
result = top_two[0][1] * top_two[1][1]
print(f"The top two monkeys inspected items {top_two[0][1]} and {top_two[1][1]} times respectively, the amount of monkey buisness: {result}")

