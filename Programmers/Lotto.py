# 프로그래머스 레벨 1 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    correct = 0
    answer = []
    
    for i in lottos:
        if i in win_nums:
            correct += 1
        
    if correct == 6:
        answer.append(1)
    elif correct == 5:
        answer.append(2)
    elif correct == 4:
        answer.append(3)
    elif correct == 3:
        answer.append(4)
    elif correct == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    correct += lottos.count(0)
    
    if correct == 6:
        answer.append(1)
    elif correct == 5:
        answer.append(2)
    elif correct == 4:
        answer.append(3)
    elif correct == 3:
        answer.append(4)
    elif correct == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    answer.sort()
    
    return answer

# 더 좋은 방법이 있을 것 같지만, 일단은 간단하고 직관적으로 작성