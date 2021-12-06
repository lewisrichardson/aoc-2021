file = 'input'

def read_fish():
    with open(file) as f:    
        return list(map(int, f.readline().split(",")))


def count_fish(fish):
    counts = [0] * 9
    
    for f in fish:
        counts[f] += 1
    for _ in range(256):
        fish_zeros = counts[0]
        counts = counts[1:] + [fish_zeros]
        counts[6] += fish_zeros
        
    print(sum(counts))

fish = read_fish()
count_fish(fish)
