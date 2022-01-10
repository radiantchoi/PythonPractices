# 프로그래머스 코딩테스트 연습 레벨 1 약수의 합

def solution(n):
    result = []
    
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)

    return sum(result)

# 약수는 자기 자신도 포함한다는 것을 기억하자.
# 꽤나 비효율적인 시간복잡도를 지닌 풀이라고 생각한다.