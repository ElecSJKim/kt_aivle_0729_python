data = []

temp = 0

while True:
    temp = input("원소를 입력해주세요")
    if temp == "end":
        break
    else:
        data.append(int(temp))
        
print(f"입력된 리스트는 {data} 입니다.")

for i in range(len(data)//2):
    data[i], data[-1-i] = data[-1-i], data[i]
    
print(f"역순으로 정렬된 리스트 결과는 {data} 입니다.")

