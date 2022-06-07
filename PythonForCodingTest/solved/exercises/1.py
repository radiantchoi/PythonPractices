# 이것이 취업을 위한 코딩 테스트다 p.311 모험가 길드

n = int(input())
t = list(map(int, input().split()))

def solution(n, travelers):
    travelers.sort()
    result = 0
    group = []

    index = 0
    while index < n:
        group.append(travelers[index])
        if group[-1] <= len(group):
            group = []
            result += 1
        
        index += 1

    return result

result = solution(n, t)
print(result)