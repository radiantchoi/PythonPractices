# 프로그래머스 코딩테스트 연습 레벨 1 약수의 개수와 덧셈

def solution(left, right):
    
    result = 0
    
    for n in range(left, right + 1):
        count = 0
        for m in range(1, n + 1):
            if n % m == 0:
                count += 1
        if count % 2 == 0:
            result += n
        else:
            result -= n
        
    return result

# 반복문에서 초기화될 변수 위치를 잘 집어넣은 것 같다. 앞으로 문제 풀때도 이렇게 면밀하게 가자.