# 백준 온라인 저지 11653번 소인수분해

n = int(input())
for number in range(2, n+1):
    if number > n:
        break

    while n % number == 0:
        n /= number
        print(number)
    