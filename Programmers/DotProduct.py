# 프로그래머스 코딩테스트 연습 레벨 1 내적

def solution(a, b):
    result = []
    
    for i in range(len(a)):
        result.append(a[i]*b[i])
    
    return sum(result)
