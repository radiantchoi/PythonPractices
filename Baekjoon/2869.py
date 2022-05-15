# 백준 온라인 저지 2869번 달팽이는 올라가고 싶다
from math import ceil

a, b, v = map(int, input().split())

target = v - b
days = target / (a - b)
print(ceil(days))

# 참조 링크 : https://yoonsang-it.tistory.com/9