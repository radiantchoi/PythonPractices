# 이것이 취업을 위한 코딩 테스트다 p.313 문자열 뒤집기

data = input()

def solution(s):
    zero = 0
    one = 0

    if s[0] == "0":
        zero += 1
    else:
        one += 1
    
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if s[i] == "0":
                zero += 1
            else:
                one += 1
        else:
            continue
    
    return min(zero, one)

result = solution(data)
print(result)