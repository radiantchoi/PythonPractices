# 이것이 취업을 위한 코딩 테스트다 p.360 안테나
# 백준 온라인 저지 주소 : https://www.acmicpc.net/problem/18310
# 제한시간 20분

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
print(nums[(n - 1) // 2])
