from enum import Enum
import numpy as np

file = 'input'
x1 = 0
y1 = 1
x2 = 2
y2 = 3

class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL_DOWN_PERFECT = 2
    DIAGONAL_UP_PERFECT = 3
    DIAGONAL_DOWN_IMPERFECT = 4
    DIAGONAL_UP_IMPERFECT = 5

def read_coorindates():
    coords_list = []
    max_width = 0
    max_height = 0

    with open(file) as f:    
        for x in f:
            coords = [int(i) for i in x.replace(' -> ', ',').rstrip().split(',')]

            if is_line(coords):
                coords_list.append(coords)
                width = max(coords[::2])
                height = max(coords[1::2])

                max_width = width if width > max_width else max_width
                max_height = height if height > max_height else max_height

    return coords_list, max_width + 1, max_height + 1

def count_overlaps(width: int, height: int, coords_list: list):
    matrix = np.zeros((width, height))

    for coords in coords_list:
        dir = direction(coords)
        
        if dir == Direction.HORIZONTAL:
            first, second = get_ordered_coords(coords[x1], coords[x2])
            for i in range(first, second):
                matrix[coords[y1], i] += 1
        
        elif dir == Direction.VERTICAL:
            first, second = get_ordered_coords(coords[y1], coords[y2])
            for i in range(first, second):
                matrix[i, coords[x1]] += 1

        elif dir == Direction.DIAGONAL_UP_PERFECT:
            coords = get_ordered_diagonal_up_coords(coords)
            
            for i in range(coords[x1], coords[x2] + 1):

                matrix[coords[y1]][coords[x1]] += 1
                coords[x1] += 1
                coords[y1] -= 1

        elif dir == Direction.DIAGONAL_DOWN_PERFECT:
            coords = get_ordered_diagonal_down_coords(coords)
                
            for i in range(coords[x1], coords[x2] + 1):
                matrix[coords[y1]][coords[x1]] += 1
                coords[x1] += 1
                coords[y1] += 1

        else:
            raise Exception('Coordinates do not contain straight line')

    return (matrix >= 2).sum()

def is_line(coords):
    return any([
        coords[x1] == coords[x2],
        coords[y1] == coords[y2],
        coords[x1] == coords[y1] and coords[x2] == coords[y2] or (coords[x1] - coords[x2] == coords[y1] - coords[y2]),
        coords[x1] == coords[y2] and coords[x2] == coords[y1] or ((coords[x1] - coords[x2]) == -(coords[y1] - coords[y2]) or -(coords[x1] - coords[x2]) == (coords[y1] - coords[y2]))
    ])

def direction(coords: list):
    if coords[x1] == coords[x2]:
        return Direction.VERTICAL
    
    if coords[y1] == coords[y2]:
        return Direction.HORIZONTAL
    
    if coords[x1] == coords[y1] and coords[x2] == coords[y2] or (coords[x1] - coords[x2] == coords[y1] - coords[y2]):
        return Direction.DIAGONAL_DOWN_PERFECT

    elif coords[x1] == coords[y2] and coords[x2] == coords[y1] or ((coords[x1] - coords[x2]) == -(coords[y1] - coords[y2]) or -(coords[x1] - coords[x2]) == (coords[y1] - coords[y2])):
        return Direction.DIAGONAL_UP_PERFECT

def get_ordered_coords(c1, c2):
    return (c1, c2 + 1) if c1 < c2 else (c2, c1 + 1)

def get_ordered_diagonal_up_coords(coords):
    return [coords[x2], coords[y2], coords[x1], coords[y1]] if coords[x1] > coords[x2] else coords

def get_ordered_diagonal_down_coords(coords):
    return [coords[x2], coords[y2], coords[x1], coords[y1]] if coords[y1] > coords[y2] else coords

def get_first_coord(a, b):
    return [a, b] if a < b else [b, a]

coordinates, width, height = read_coorindates()
overlaps = count_overlaps(width, height, coordinates)
print(f'overlaps: {overlaps}')
