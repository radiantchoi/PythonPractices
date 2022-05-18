# 백준 온라인 저지 4948번 베르트랑 공준
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

nums = list(range(2, 250000))
primes = [x for x in nums if isPrime(x)]

while True:
    n = int(input())
    if n == 0:
        break
    
    result = 0
    for number in primes:
        if n < number <= 2*n:
            result += 1
    
    print(result)

# 참조 : https://velog.io/@iillyy/%EB%B0%B1%EC%A4%80-4948%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC