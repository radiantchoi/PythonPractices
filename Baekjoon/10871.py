# 백준 온라인 저지 10871번 X보다 작은 수

n, x = map(int, input().split())
nums = list(map(int, input().split()))

for num in nums:
    if num < x:
        print(num, end=" ")