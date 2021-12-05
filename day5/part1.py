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

def read_coorindates():
    coords_list = []
    max_width = 0
    max_height = 0

    with open(file) as f:    
        for x in f:
            coords = [int(i) for i in x.replace(' -> ', ',').rstrip().split(',')]

            if is_straight_line(coords):
                coords_list.append(coords)
                width = max(coords[::2])
                height = max(coords[1::2])

                max_width = width if width > max_width else max_width
                max_height = height if height > max_height else max_height

    return coords_list, max_width + 1, max_height + 1

def count_overlaps(width: int, height: int, coords_list: list):
    matrix = np.zeros((width, height))
    print(coords_list)
    for coords in coords_list:
        dir = direction(coords)
        
        if dir == Direction.HORIZONTAL:
            first, second = (coords[x1], coords[x2]) if coords[x1] < coords[x2] else (coords[x2], coords[x1])
            for i in range(first, second + 1):
                matrix[coords[y1], i] += 1
        
        elif dir == Direction.VERTICAL:
            first, second = (coords[y1], coords[y2]) if coords[y1] < coords[y2] else (coords[y2], coords[y1])
            print(first, second)
            for i in range(first, second + 1):
                matrix[i, coords[x1]] += 1

        else:
            raise Exception('Coordinates do not contain straight line')

    return (matrix >= 2).sum()

def is_straight_line(coords):
    return coords[x1] == coords[x2] or coords[y1] == coords[y2]

def direction(coords: list):
    return Direction.HORIZONTAL if coords[y1] == coords[y2] else Direction.VERTICAL

coordinates, width, height = read_coorindates()
overlaps = count_overlaps(width, height, coordinates)
print(f'overlaps: {overlaps}')
