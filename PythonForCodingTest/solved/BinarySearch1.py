# 이것이 취업을 위한 코딩 테스트다 p.197 부품 찾기

n = int(input())
pieces = list(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))

def solution(pieces, requests):
    pieces.sort()

    def search(arr, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif mid > target:
                end = mid - 1
            else:
                start = mid + 1
        return None

    answer = []    
    for request in requests:
        result = search(pieces, request, 0, len(pieces)-1)
        if result == None:
            answer.append("no")
        else:
            answer.append("yes")
    
    return answer

print(solution(pieces, requests))

# 괜히 재귀를 활용한 이진 탐색 시도한다고 깝치지 말고, 반복문을 활용한 이진 탐색으로 가자.