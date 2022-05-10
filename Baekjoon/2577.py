# 백준 온라인 저지 2577번 숫자의 개수

n = 1
for i in range(3):
    n *= int(input())

raw = str(n)
numbers = [0] * 10

for i in range(len(raw)):
    j = int(raw[i])
    numbers[j] += 1

for n in numbers:
    print(n)