# 이것이 취업을 위한 코딩 테스트다 p.322 문자열 재정렬

data = input()

def solution(s):
    nums = []
    alpha = []

    for i in range(len(s)):
        if 64 < ord(s[i]) < 91:
            alpha.append(s[i])
        else:
            nums.append(int(s[i]))
    
    alpha.sort()
    result = "".join(alpha)
    if nums:
        result += str(sum(nums))
    
    return result

result = solution(data)
print(result)

# isalpha 썼어도 괜찮을 뻔 했다~