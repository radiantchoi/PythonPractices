# 프로그래머스 코딩테스트 연습 레벨 2 피보나치 수

def solution(n):
    results = [0] * (n+1)
    results[1] = 1
    results[2] = 1

    for i in range(3, n+1):
        if results[i] == 0:
            results[i] = results[i-2] + results[i-1]
        else:
            continue

    return results[-1] % 1234567

# 다이나믹 프로그래밍의 원리를 보여주는 가장 기본적인 문제이다. 반복 학습을 통해 익히자.
# 메모이제이션을 활용했다.