# 프로그래머스 코딩테스트 연습 레벨 2 프린터

from collections import deque

def solution(priorities, location):
    indicator = deque([0] * len(priorities))
    indicator[location] = 1
    count = 0
    q = deque(priorities)
    
    while q:
        current = q.popleft()
        mark = indicator.popleft()
        if not q: # 지금 뽑아둔 게 마지막 원소일 경우
            count += 1 # 어쨌든 얘를 인쇄했다는 카운트는 세야 하므로
            break # 무한루프를 방지하기 위한 while 탈출
        else:
            if max(q) > current:
                q.append(current)
                indicator.append(mark)
            else:
                count += 1
                if mark == 1:
                    break
    
    return count

# 잘한 점 : indicator를 지정해서 표본을 잘 뽑아낸 점
# 보완해야 할 점 : q의 원소가 1개 남을 때 무한루프를 돈다는 것을 캐치하지 못한 점