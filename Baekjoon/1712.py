# 백준 온라인 저지 1712번 손익분기점

a, b, c = map(int, input().split())

cost = b - c
if cost >= 0:
    print(-1)
else:
    profit = -cost
    result = (a // profit) + 1
    print(result)