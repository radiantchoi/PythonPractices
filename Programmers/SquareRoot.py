# 프로그래머스 코딩 테스트 연습 레벨 1 정수 제곱근 판별

import math

def solution(n):
    answer = 0
    
    if math.sqrt(n) % 1 == 0:
        answer = (math.sqrt(n) + 1) ** 2
    else:
        answer = -1

    return answer

# math 모듈의 사용에 관한 문제인 듯 하다.
# 파이썬에서 나눗셈 연산 중, 소수점 아래도 나머지로 치는지 개인적으로 실험해보는 의미도 있었는데, 추측이 맞은 듯 하다.