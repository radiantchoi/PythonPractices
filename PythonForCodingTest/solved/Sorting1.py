# 이것이 취업을 위한 코딩 테스트다 p.178 위에서 아래로

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
for number in arr:
    print(number, end=" ")