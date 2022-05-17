# 백준 온라인 저지 1978번 소수 찾기
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    
    return True

n = int(input())
datas = map(int, input().split())
result = [x for x in datas if isPrime(x)]

print(len(result))