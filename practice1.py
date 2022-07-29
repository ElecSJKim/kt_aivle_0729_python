num = [2]

for i in range(3, 1001):
    temp = 0
    for j in range(2, i):
        if i % j == 0:
            temp = 1
            break
        
    if temp == 0:
        num.append(i)
    
print(num)
        
        