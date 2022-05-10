# 백준 온라인 저지 11720번 숫자의 합

n = int(input())
result = 0
data = input()
for i in range(n):
    result += int(data[i])

print(result)