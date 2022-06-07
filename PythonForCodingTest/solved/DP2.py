# 이것이 취업을 위한 코딩 테스트다 p.220 개미 전사

n = int(input())
arr = list(map(int, input().split()))

def solution(cargo):
    for i in range(2, len(cargo)):
        cargo[i] += max(cargo[:i-1])
    
    return max(cargo)

print(solution(arr))

# 릿코드에서 풀어봤던 경험이 있다보니 좀 더 쉽게 푼 듯?