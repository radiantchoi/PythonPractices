# 프로그래머스 코딩테스트 연습 레벨 1 두 정수 사이의 합

def solution(a, b):
    
    result = 0
    
    if a < b:
        for n in range(a, b+1):
            result += n
    elif a > b:
        for n in range(b, a+1):
            result += n
    else:
        result += a # b여도 되겠지만
    
    return result
