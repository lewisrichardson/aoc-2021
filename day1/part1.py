f = open('input')

last = None
current = 0
increase = 0
decrease = 0

for x in f:
    if last == None:
        last = int(x)
        continue
    
    current = int(x)
    if current > last:
        increase += 1
    elif last > current:
        decrease +=1
        
    last = current

print(f'increase: {increase}')
print(f'decrease: {decrease}')
