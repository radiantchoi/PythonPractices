# 이것이 취업을 위한 코딩 테스트다 p.346 괄호 변환
# 프로그래머스 주소 : https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    if not p:
        return ""
    
    result = ""

    left = 0
    right = 0
    u = ""
    index = 0
    while (left == 0 and right == 0) or left != right:
        letter = p[index]
        u += letter
        if letter == "(":
            left += 1
        else:
            right += 1
        
        index += 1

    v = p[index:]

    if iscorrect(u):
        result = u + solution(v)
    else:
        result += "("
        result += solution(v)
        result += ")"

        for i in range(1, len(u)-1):
            if u[i] == "(":
                result += ")"
            else:
                result += "("
    
    return result

def iscorrect(u):
    left = 0
    right = 0

    for i in range(len(u)):
        if u[i] == "(":
            left += 1
        else:
            right += 1
        
        if left < right:
            return False
    
    return True