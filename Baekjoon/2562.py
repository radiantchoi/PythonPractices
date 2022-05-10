# 백준 온라인 저지 2562번 최댓값

n = 0
c = 0

for i in range(1, 10):
    num = int(input())
    if num > n:
        n = num
        c = i

print(n)
print(c)