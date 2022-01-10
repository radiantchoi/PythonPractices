# 프로그래머스 코딩테스트 연습 레벨 1 소수 찾기

import math

def solution(n):
    count = 0
    prime = [True for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i] == True:
            j = 2
            while i*j <= n:
                prime[i*j] = False
                j += 1
    
    for k in range(2, n+1):
        if prime[k]:
            count += 1
    
    return count

# 에라토스테네스의 체를 연습하기 위해 풀어 보았다. 해당 코드는 손에 익을 때까지 연습하자.