# 이것이 취업을 위한 코딩 테스트다 p.201 떡볶이 떡 만들기

n, m = map(int, input().split())
rices = list(map(int, input().split()))

def solution(rices, request):
    # request * len(rices): 손실되는 떡의 길이
    # sum(rices): 떡의 총 길이
    # 단, 칼날이 떡보다 위에 있으면 그냥 0 (이 조건이 중요)
    # 자료의 갯수는 백만개, 길이는 각각 0부터 10억까지 가능
    # 칼날의 길이가 얼마여야, 떡을 리퀘스트 이상 잘라낼 수 있을 것인가??
    # 가능한 칼날의 길이 값을 이진 탐색으로 찾는다.
    # 백만 곱하기 서른두 번 정도?

    # blades = list(range(1000000001)) 
    blades = list(range(max(rices))) # 범위를 그렇게 넓게 안 잡아도 된다..

    def cut(rices, blade, target):
        result = 0
        for rice in rices:
            if rice - blade > 0:
                result += rice - blade
        
        if result == target:
            return 0
        elif result > target:
            return 1
        else:
            return -1

    start = 0
    end = len(blades)-1
    index = 0
    while start < end:
        mid = (start + end) // 2
        if cut(rices, blades[mid], request) == 0:
            index = mid
        elif cut(rices, blades[mid], request) > 0:
            end = mid - 1
        else:
            start = mid + 1

    return blades[index]

print(solution(rices, m))

# 무한으로 입력을 받아버리는 오류에 대해서 찾아봐야겠다.
# 방법론은 맞았음. 단, 위쪽에 칼 길이 정해주는 부분만 너무 과했다.