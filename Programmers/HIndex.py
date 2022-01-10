# 프로그래머스 코딩테스트 연습 레벨 2 H-Index

def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(len(citations)):
        if citations[i] >= len(citations[i:]):
            answer = len(citations[i:])
            break
    
    return answer

# 정렬 문제지만 정작 정렬은 내장 정렬을 쓰면 된다니..
# break를 넣어줘야 딱 만나는 지점에서 멈추고 결과가 출력된다. 안 그러면 오직 1만 답으로 얻게 될 것..
# 스위프트로 짰을 때보다 실력이 늘었음을 느낀다.