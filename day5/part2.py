from enum import Enum
import numpy as np

file = 'input'
x1 = 0
y1 = 1
x2 = 2
y2 = 3

class Direction(Enum):
    NONE = 0
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL_DOWN = 3
    DIAGONAL_UP = 4
    
class CoordinateData:    
    def __init__(self, coords, dir):
        self.coords = coords
        self.dir = dir

def read_coorindates():
    coords_data = []
    max_width = 0
    max_height = 0

    with open(file) as f:    
        for x in f:
            coords = [int(i) for i in x.replace(' -> ', ',').rstrip().split(',')]
            dir = get_direction(coords)
            coords_data.append(CoordinateData(coords, dir))
            
            width = max(coords[::2])
            height = max(coords[1::2])

            max_width = width if width > max_width else max_width
            max_height = height if height > max_height else max_height

    return coords_data, max_width + 1, max_height + 1

def count_overlaps(width: int, height: int, coords_data: list):
    matrix = np.zeros((width, height))

    for data in coords_data:
        coords = data.coords
        
        match data.dir:
            case Direction.HORIZONTAL:
                first, second = get_ordered_coords(coords[x1], coords[x2])
                for i in range(first, second):
                    matrix[coords[y1], i] += 1
            
            case Direction.VERTICAL:
                first, second = get_ordered_coords(coords[y1], coords[y2])
                for i in range(first, second):
                    matrix[i, coords[x1]] += 1

            case Direction.DIAGONAL_UP:
                coords = get_ordered_diagonal_up_coords(coords)
                
                for i in range(coords[x1], coords[x2] + 1):

                    matrix[coords[y1]][coords[x1]] += 1
                    coords[x1] += 1
                    coords[y1] -= 1

            case Direction.DIAGONAL_DOWN:
                coords = get_ordered_diagonal_down_coords(coords)
                    
                for i in range(coords[x1], coords[x2] + 1):
                    matrix[coords[y1]][coords[x1]] += 1
                    coords[x1] += 1
                    coords[y1] += 1

    return (matrix >= 2).sum()

def get_direction(coords: list):
    if coords[x1] == coords[x2]:
        return Direction.VERTICAL
    
    if coords[y1] == coords[y2]:
        return Direction.HORIZONTAL
    
    if coords[x1] == coords[y1] and coords[x2] == coords[y2] or
        (coords[x1] - coords[x2] == coords[y1] - coords[y2]):
        return Direction.DIAGONAL_DOWN

    elif coords[x1] == coords[y2] and coords[x2] == coords[y1] or
        ((coords[x1] - coords[x2]) == -(coords[y1] - coords[y2]) or -(coords[x1] - coords[x2]) == (coords[y1] - coords[y2])):
        return Direction.DIAGONAL_UP

def get_ordered_coords(c1, c2):
    return (c1, c2 + 1) if c1 < c2 else (c2, c1 + 1)

def get_ordered_diagonal_up_coords(coords):
    return [coords[x2], coords[y2], coords[x1], coords[y1]] if coords[x1] > coords[x2] else coords

def get_ordered_diagonal_down_coords(coords):
    return [coords[x2], coords[y2], coords[x1], coords[y1]] if coords[y1] > coords[y2] else coords

coordinates, width, height = read_coorindates()
overlaps = count_overlaps(width, height, coordinates)
print(f'overlaps: {overlaps}')
