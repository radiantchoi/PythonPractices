# 백준 온라인 저지 2908번 상수

a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
print(max(a, b))