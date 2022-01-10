# 프로그래머스 코딩테스트 연습 레벨 1 자릿수 더하기

def solution(n):
    digit = list(str(n))
    digits = []
    for i in digit:
        digits.append(int(i))
    
    return sum(digits)

# 수를 리스트에 뿌려 주는 거 연습할 겸 간단히 풀어 보았다.