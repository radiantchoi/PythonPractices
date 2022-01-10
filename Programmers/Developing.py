# 프로그래머스 코딩테스트 연습 레벨 2 기능개발
# 참고한 풀이 = https://programmers.co.kr/questions/16191

from collections import deque

def solution(progresses, speeds):
    answer = []
    prgq = deque(progresses)
    spdq = deque(speeds)
    daily = 0
    
    if len(progresses) == 1:
        return 1
    
    while True:
        for i in range(len(prgq)):
            prgq[i] += spdq[i]
            
        if prgq[0] >= 100:
            while prgq[0] >= 100:
                prgq.popleft()
                prgq.append(0)
                spdq.popleft()
                spdq.append(0)
                daily += 1
                if prgq[0] < 100:
                    answer.append(daily)
                    daily = 0
                    
        if prgq[0] == 0:
            break
    
    return answer

# 잘한 점 = 0을 append해줌으로써 index out of range를 방지한 것, 큐의 첫 원소만 0인지 봐서 큐가 비었는지 판별한 것
# 보완해야 할 점 = while문 속 if문, 즉 큐의 첫 원소가 100이 넘는지를 체크하는 if의 위치.
# 처음에는 for문 아래에 두었으나, 그렇게 하면 [99, 99, 99], [1, 1, 1] 케이스에서 [3]이 아닌 [1, 2]가 나왔다.
# 애시당초 딱 100이 아니라 100이 넘으면 popleft하도록 짰으니, 일단 전체적으로 spdq만큼 더해준 다음 뽑으면 될 것을
# 괜히 for문 아래에 둬서 첫 케이스만 따로 뽑히게 만들었다.. 
# 사실 왜 그런진 모르나, 그럴 필요가 없는 부분을 쳐내고 올바른 흐름을 만드니 문제가 해결된 것에 가깝다.
# 흐름에 대해 주의하고, 들여쓰기를 올바로 하자.