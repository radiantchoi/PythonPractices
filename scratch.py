from math import comb

i = int(input())

for case in range(i):
    n, m = map(int, input().split())
    print(comb(m, n))