# 이것이 취업을 위한 코딩 테스트다 p.182 두 배열의 원소 교체

n, k = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

def solution(first, second, k):
    first.sort(reverse=True)
    second.sort()

    storage = []
    while k > 0:
        first.pop()
        storage.append(second.pop())
        k -= 1
    
    first += storage
    return sum(first)

print(solution(first, second, k))
