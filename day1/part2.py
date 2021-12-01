f = open('numbers')

a = []
b = []
increase = 0

for x in f:
    if len(a) < 3:
        a.append(int(x))
        continue
    
    elif len(a) == 3 and len(b) == 0:
        b.extend([a[1], a[2], int(x)])
        if sum(b) > sum(a):
            increase += 1
        continue
    
    if (len(a) == 3 and len(b) == 3):
        del a[0]
        a.append(b[-1])
        del b[0]
        b.append(int(x))
        
        if sum(b) > sum(a):
            increase += 1


print(f'increase: {increase}')
