print("리스트를 역순으로 출력합니다")
num = int(input("원소 수를 입력하세요.: "))

x = [0]*num
for i in range(len(x)):
    x[i] = int(input(f"x[{i}]값을 입력하세요: "))
    
for i in range(len(x)//2):
    x[i], x[-1-i] = x[-1-i], x[i]

print("리스트를 역순으로 출력합니다.")    
for i in range(len(x)):
    print(f"x[{i}] = {x[i]}")
    
