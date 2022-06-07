# 이것이 취업을 위한 코딩 테스트다 p.92 큰 수의 법칙

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

def solution(n, m, k, nums) -> int:
    nums.sort()
    first = nums.pop()
    second = nums.pop()

    indicator = k
    result = 0

    while m > 0:
        if indicator == 0:
            result += second
            indicator = k
        else:
            result += first
            indicator -= 1
        
        m -= 1
    
    return result

print(solution(n, m, k, nums))