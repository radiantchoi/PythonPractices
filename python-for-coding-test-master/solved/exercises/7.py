# 이것이 취업을 위한 코딩 테스트다 p.321 럭키 스트레이트
# 백준 온라인 저지 주소 : https://www.acmicpc.net/problem/18406

data = input()

def solution(s):
    left = 0
    right = 0

    crit = len(s) / 2
    for i in range(len(s)):
        if i < crit:
            left += int(s[i])
        else:
            right += int(s[i])
    
    if left == right:
        return "LUCKY"
    else:
        return "READY"

result = solution(data)
print(result)