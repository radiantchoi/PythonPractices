# 프로그래머스 코딩테스트 연습 레벨 2 N개의 최소공배수

import math

def solution(arr):
    arr.sort()
    answer = arr[0]
    for i in range(1, len(arr)):
        if answer % arr[i] == 0:
            continue
        else:
            if arr[i] % answer == 0:
                answer = arr[i]
            else:
                x = int(answer * arr[i] / math.gcd(answer, arr[i]))
                answer = x

    return answer

# 이중 if를 통해 어렵지 않게 풀 수 있었다.