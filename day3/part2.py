from enum import Enum
from typing import List

class Rating(Enum):
    OXYGEN_GENERATOR = 0,
    CO2_SCRUBBER = 1

def read_lines() -> List[str]:
    with open('input') as f:
        lines = f.read().split('\n')
        del lines[-1] # remove empty line
        return lines

def calculate_rating(rating_type: Rating) -> int:
    lines = read_lines()
    for column_index in range(12):
        count = [0, 0]
        
        for current_num in lines:
            digit = current_num[column_index]
            count[0 if int(digit) == 0 else 1] += 1
            
        keep_bit = 1 if rating_type == Rating.OXYGEN_GENERATOR else 0
        inverse_bit = 1 if keep_bit == 0 else 0
        value_to_keep = keep_bit if count[0] == count[1] or count[0] < count[1] else inverse_bit
        
        lines = [
            num for num in lines
            if int(num[column_index]) == value_to_keep
        ]
        if len(lines) == 1:
            return int(lines[0], 2)

int_oxygen_generator_rating = calculate_rating(Rating.OXYGEN_GENERATOR)
int_co2_scrubber_rating = calculate_rating(Rating.CO2_SCRUBBER)
life_support_rating = int(int_oxygen_generator_rating * int_co2_scrubber_rating)
print(f'life support rating: {life_support_rating}')
