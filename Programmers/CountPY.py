# 프로그래머스 코딩테스트 연습 1레벨 문자열 내 p와 y의 개수

def solution(s):
    result = True
    countp = 0
    county = 0
    
    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            countp += 1
        elif s[i] == "y" or s[i] == "Y":
            county += 1
        
    if countp == county:
        result = True
    else:
        result = False

    return result

# 평범한 문제지만.. 문자열 인덱싱과 대소문자 구별 연습 했다고 생각한다.