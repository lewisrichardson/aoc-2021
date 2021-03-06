h_pos = 0
depth = 0
aim = 0

f = open('input')
for x in f:
    split_string = x.split()
    direction = split_string[0]
    direction_value = int(split_string[1])
    
    match direction:
        case 'forward':
            h_pos += direction_value
            depth += aim * direction_value
        case 'up':
            aim -= direction_value
        case 'down':
            aim += direction_value
            
print(f'horizontal position: {h_pos}')
print(f'depth: {depth}')
print(f'result: {h_pos * depth}')
