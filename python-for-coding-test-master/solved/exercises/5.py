# 이것이 취업을 위한 코딩 테스트다 p.315 볼링공 고르기

number, max = map(int, input().split())
balls = list(map(int, input().split()))

def solution(number, max, balls):
    result = 0

    weights = [0] * (max + 1)
    for ball in balls:
        weights[ball] += 1
    
    for ball in balls:
        result += number - weights[ball]
    
    result /= 2
    return int(result)

result = solution(number, max, balls)
print(result)
