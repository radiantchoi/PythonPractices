# 프로그래머스 코딩테스트 연습 레벨 1 음양 더하기

def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    
    answer = sum(absolutes)
    return answer