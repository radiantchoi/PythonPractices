# 프로그래머스 코딩테스트 연습 레벨 1 같은 숫자는 싫어

def solution(arr):

    result = []

    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]: # 앞의 것과 같으면 넣지 않는다. 최대한 직관적으로
            continue
        else:
            result.append(arr[i])

    result.insert(0, arr[0]) 
    # 이미 위의 for문에서, arr[0]과 arr[1]을 비교해서 같다면 arr[1]은 안들어갔을 거기 때문에

    return result

# 파이썬 기본 문법 연습도 해야 할 듯 하다.
# 알아둘 것: insert