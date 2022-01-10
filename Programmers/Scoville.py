# 프로그래머스 코딩테스트 연습 레벨 2 더 맵게

import heapq

def solution(scoville, K):
    count = 0
    scoville.sort()
    
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        if a > K and b > K:
            break
        
        new = a + 2 * b
        count += 1
        heapq.heappush(scoville, new)
        if new > K and scoville[0] > K:
            break
        
    if len(scoville) == 1 and scoville[0] < K:
        count = -1
        
    return count

# 고려할 것 : 기본적으로 입력되는 리스트의 정렬, 처음부터 스코빌 수치가 다 만족할 때, 루프 안에서 딱 맞춰서 조건 만족할 때
# 1번 케이스는 heapify를 쓰든 sort를 쓰든 크게 상관이 없는 듯 했다. sort가 조금 더 시간 효율이 좋군
# 2번 케이스는 뽑아 온 a와 b 값을 검사했다.
# 3번 케이스는, 원래 if문 뒤에 왔던 heappush를 앞으로 당김으로써, 리스트가 비지 않을 것을 보장했다.
# 3번의 경우, 두 개만 딱 남고 그걸 섞으면 조건이 만족되는 경우, 순간적으로 리스트가 비기 때문에 이를 해결하고자..
# 반복문 안에서의 원소의 흐름을 잘 생각하는 것이 좋을 것 같다.