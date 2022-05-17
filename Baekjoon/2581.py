# 백준 온라인 저지 2581번 소수
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

m = int(input())
n = int(input())
primes = [x for x in range(m, n+1) if isPrime(x)]

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)