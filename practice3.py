def seq_search_sentinel(data, target):
    a = list(data)
    a.append(target)
    
    i = 0
    while True:
        if a[i] == target:
            break
        i += 1
        
    return -1 if i == len(data) else i

data = list(map(int, input("리스트를 입력해주세요").split()))
target = int(input("검색할 값을 입력해주세요"))

index = seq_search_sentinel(data, target)

if index == -1:
    print("검색값을 갖는 원소가 존재하지 않습니다.")
else:
    print(f"검색값은 data[{index}]에 있습니다.")
