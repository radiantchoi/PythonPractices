# 백준 온라인 저지 10951번 A + B - 4

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# ---

import sys

data = sys.stdin.readlines()
for line in data:
    a, b = map(int, line.split())
    print(a+b)

# EOF 개념은 내가 모르는 것이었고, 이 참에 배워간다. End Of File.
# 파이썬에서는 오류 처리를 저렇게 하는구나 하는 것도 잘 봤다.
# readlines()는 점투파 할 때 봤던 것 같은데, 막상 보니 기억이 안 났다고나 할까..