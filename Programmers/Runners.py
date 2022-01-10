# 프로그래머스 코딩테스트 연습 레벨 1 완주하지 못한 선수

# 참고한 풀이 : https://ychae-leah.tistory.com/24

def solution(participant, completion):

    participant.sort()
    completion.sort()
                
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    return participant.pop()

# 알아두어야 할 것 : zip (같은 인덱스의 항목끼리 짝지어주는 함수)
# return이 두 개 있잖아? 다 짝지어놓고 나서, 남은 친구가 있으면 pop으로 나오게 하고, 다른 항목이 있으면 지원자를 return하는 것