data = list(map(int, input("리스트를 입력하세요").split()))

maxnum = data[0]
index = 0

for i in range(1, len(data)):
    if data[i] > maxnum:
        maxnum = data[i]
        index = i
        
print(f"최대값은 {data[index]}이고, 해당 인덱스는 {index} 입니다.")