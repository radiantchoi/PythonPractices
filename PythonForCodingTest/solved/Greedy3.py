# 이것이 취업을 위한 코딩 테스트다 p.99 1이 될 때까지

n, k = map(int, input().split())

def solution(n, k) -> int:
    estimated = 0

    while n > 1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        
        estimated += 1

    return estimated

print(solution(n, k))