values = []

with open('input') as f:
    line = f.readline()
    values = [[0,0] for _ in range (len(line) - 1)]

with open('input') as f:
    for x in f:
        digits = [int(digit) for digit in x.rstrip()]
        
        for i, digit in enumerate(digits):
            values[i][0 if digit == 0 else 1] += 1

gamma_rate = ''
for tuple in values:
    gamma_rate += '0' if tuple[0] > tuple[1] else '1'

epsilson_rate = ''.join(['1' if i == '0' else '0' for i in gamma_rate])
power_consumption = int(gamma_rate, 2) * int(epsilson_rate, 2)
print(f'power consumption: {power_consumption}')
