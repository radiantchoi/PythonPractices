# 이것이 취업을 위한 코딩 테스트다 p.323 문자열 압축
# 프로그래머스 주소 : https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    lengths = []
    
    length = 1
    while length <= len(s):
        result = check(length, s)
        lengths.append(len(result))
        length += 1
    
    return min(lengths)

def check(length, s):
    result = ""
    current = s[0:length]
    count = 1
    
    for i in range(length, len(s), length):
        snippet = s[i:i+length]
        if snippet == current:
            count += 1
        else:
            if count > 1:
                result += str(count)
            count = 1
            result += current
            current = snippet
    
    if count > 1:
        result += str(count)
    result += current
        
    return result