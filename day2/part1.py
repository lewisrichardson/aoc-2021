h_pos = 0
depth = 0

f = open('input')
for x in f:
    split_string = x.split()
    direction = split_string[0]
    direction_value = int(split_string[1])
    
    match split_string[0]:
        case 'forward':
            h_pos += direction_value
        case 'up':
            depth -= direction_value
        case 'down':
            depth += direction_value
            
print(f'horizontal position: {h_pos}')
print(f'depth: {depth}')
print(f'result: {h_pos * depth}')
