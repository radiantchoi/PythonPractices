# 프로그래머스 코딩테스트 연습 레벨 1 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    answer.sort()
    
    if len(answer) == 0:
        answer.append(-1)
    
    return answer

# 진짜 간단한 문제긴 한데, 아직도 연산자가 헷갈린다. 스위프트랑 같이 해서 그렇겠지?
# 파이썬의 나누기는 /, 몫은 //, 나머지는 %이다.