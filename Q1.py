# Q1 Answer template

def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    win_count = 0
    score = [6, 6, 5, 4, 3, 2, 1]
    
    for i in lottos:
        if i in win_nums:
            win_count += 1
        elif i == 0:
            zero_count += 1
            
    answer.append(score[win_count+zero_count])
    answer.append(score[win_count])    
        
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)