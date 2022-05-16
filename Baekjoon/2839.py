# 백준 온라인 저지 2839번 설탕 배달

n = int(input())

def solution(n):
    x = n // 5
    y = 0
    rest = n % 5

    while rest % 3 != 0:
        rest += 5
        x -= 1
        if x < 0:
            return -1
    
    y = rest // 3
    return x + y

print(solution(n))