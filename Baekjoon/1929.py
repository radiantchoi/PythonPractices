# 백준 온라인 저지 1929번 소수 구하기
from math import sqrt

m, n = map(int, input().split())

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

for number in range(m, n + 1):
    if isPrime(number):
        print(number)