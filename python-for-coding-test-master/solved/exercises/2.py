# 이것이 취업을 위한 코딩 테스트다 p.312 곱하기 혹은 더하기
data = input()

def solution(s):
    i = 0
    while int(s[i]) == 0:
        i += 1
    
    result = int(s[i])
    i += 1

    while i < len(s):
        value = int(s[i])

        if value <= 1: # 값이 1일 경우를 생각을 못 했다.
            result += value
        else:
            result *= value 
        
        i += 1

    return result

result = solution(data)
print(result)