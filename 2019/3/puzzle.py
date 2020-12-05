with open('input.txt') as f:
    raw_input = f.readlines()


# wire1 = 'R8,U5,L5,D3'.split(',')
# wire2 = 'U7,R6,D4,L4'.split(',')
wire1 = raw_input[0].split(',')
wire2 = raw_input[1].split(',')
# print(len(wire1))
# print(len(wire2))

# brute force
def draw_path(instruction):
    coord = []
    x, y = (0, 0)
    for vector in instruction:
        direction = vector[0]
        magnitude = int(vector[1:])
        for i in range(magnitude):
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            coord.append((x, y))

    return coord

path1 = draw_path(wire1)
path2 = draw_path(wire2)

# print(path1)
# print(path2)

intersections = set(path1) & set(path2)
manhattan_distance = min([(abs(x[0]) + abs(x[1])) for x in intersections])
print(manhattan_distance)


''''''''''''''
''' Part 2 '''
''''''''''''''

def pedometer(path, intersection_set):
    step_count = []
    for poi in intersection_set:
        for step, coord in enumerate(path):
            if coord == poi:
                step_count.append(step)
    
    return step_count


a = pedometer(path1, intersections)
b = pedometer(path2, intersections)
print(min([x + y for x, y in zip(a, b)]) + 2)  # 2, in order to account for 0 index
