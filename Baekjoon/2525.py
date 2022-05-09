# 백준 온라인 저지 2525번 오븐 시계

h, m = map(int, input().split())
est = int(input())

now = (h * 60) + m
now += est
now = now % 1440

print(now // 60, end=" ")
print(now % 60)