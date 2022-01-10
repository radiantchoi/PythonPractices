# 프로그래머스 코딩테스트 연습 레벨 1 최대공약수와 최소공배수

from math import gcd

def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(n * m / gcd(n, m))
    return answer

# 예상대로 math 라이브러리에서 제공하는 기능..
# 알아둘 것 : math 라이브러리의 gcd, 유클리드 호제법(중에서도 a*b = 최대공약수*최소공배수)