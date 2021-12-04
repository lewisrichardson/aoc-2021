from enum import Enum
from itertools import islice
from typing import List
import numpy as np

INPUT = 'input'
CARD_DIMENSION = 5

class WonStatus(Enum):
    NOT_WON = 0,
    WON = 1

def get_draw_numbers() -> List[int]:
    with open(INPUT) as f:
        return [int(x) for x in f.readline().split(',')]

def get_bingo_cards() -> List[List[List[int]]]:
    bingo_cards = []
    with open(INPUT) as f:
        # ignore first two lines
        for _ in islice(f, 2):
            pass
        
        while True:
            bingo_card = []
            for _ in range(CARD_DIMENSION):
                line = [int(x) for x in f.readline().rstrip().split()]
                if not line:
                    return bingo_cards
                
                bingo_card.append(line)
                
            card_data = [np.array(bingo_card), WonStatus.NOT_WON]
            bingo_cards.append(card_data)
            
            # fix later
            try:
                next(f)
            except:
                pass

def find_winning_board(draw_numbers, bingo_cards):
    won_cards = []
    last_num_drawn = -1
    
    for draw_num in draw_numbers:
        for bingo_card_index, bingo_card_data in enumerate(bingo_cards):
            if bingo_card_data[1] == WonStatus.WON:
                continue
            
            found = np.where(bingo_card_data[0] == draw_num)
            if len(found[0]) != 1: continue
            bingo_card_data[0][found[0], found[1]] = -1
            
            for i in range(CARD_DIMENSION):
                row_line = bingo_card_data[0][i, :]
                column_line = bingo_card_data[0][:, i]
                if np.all(row_line == -1) or np.all(column_line == -1):
                    won_cards.append(bingo_card_data[0])
                    bingo_card_data[1] = WonStatus.WON
                    last_num_drawn = draw_num
    
    return won_cards[-1], last_num_drawn

draw_numbers = get_draw_numbers()
bingo_cards = get_bingo_cards()
winning_bingo_card, draw_number = find_winning_board(draw_numbers, bingo_cards)

sum = 0
for row in winning_bingo_card:
    for item in row:
        if item != -1:
            sum += item

final_score = sum * draw_number
print(final_score)
