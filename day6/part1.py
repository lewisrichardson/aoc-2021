import numpy as np

file = 'input'

def read_fish():
    with open(file) as f:    
        return np.array([int(x) for x in f.readline().split(',')])

def count_fish(fish):
    for _ in range(1, 257):
        fish[:] = [el - 1 for el in fish]
        
        expired = np.where(fish == -1)[0]
        if len(expired) > 0:
            fish[expired] = 6
            fish = np.append(fish, [8] * len(expired))
        
    print(f'Total fish: {len(fish)}')

fish = read_fish()
count_fish(fish)
