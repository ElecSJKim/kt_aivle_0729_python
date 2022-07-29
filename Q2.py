# Q2 Answer template

def solution(numbers):
    answer = 45
    
    for i in numbers:
        answer -= i
    
    return answer

numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
print(answer)