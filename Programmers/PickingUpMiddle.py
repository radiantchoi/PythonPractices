# 프로그래머스 코딩테스트 연습 레벨 1 가운데 글자 가져오기

def solution(s):
    result = []
    
    if len(s) % 2 != 0:
        result.append(s[int((len(s)-1)/2)])
    else:
        result.append(s[int(len(s)/2-1)])
        result.append(s[int(len(s)/2)])
        
    answer = ""
    
    return answer.join(result)

# 이게 최선인가 싶지만, 일단 알아먹기 쉬우니까..