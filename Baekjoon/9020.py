# 백준 온라인 저지 9020번 골드바흐의 추측

primes = [True] * 10001

for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        primes[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    x = n // 2

    for i in range(x, 1, -1):
        if primes[i] and primes[n - i]:
            print(i, n-i)
            break

# 참조 : https://pacific-ocean.tistory.com/129