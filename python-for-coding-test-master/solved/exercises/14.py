# 이것이 취업을 위한 코딩 테스트다 p.335 외벽 점검
# 프로그래머스 주소 : https://programmers.co.kr/learn/courses/30/lessons/60062

# 1회차 실패
# 잘 한 점 : 경우의 수 나눈 점. 가게 지도를 만들 때, 원형 배열이기 때문에 길이를 늘린 점.
# 개선해야 할 점 : 역시나 수학적 아이디어!
# 해답에서는 permutation을 사용했다. 각각의 경우의 수에서 모든 지점을 점검할 수 있는지 판별.
# 또한, 어차피 한 방향으로만 돌게 된다는 것을 상기하자!
# 모든 지점을 점검하려면, 어차피 친구들을 연속적으로 배치해야 한다.
# 그러므로 가게 지도씩이나 만들 필요가 있기보단, 배열 길이를 2배 정도로만 늘려줘도 되는 것.



# def solution(n, weak, dist):
#     store = [0] * (3 * n) # 가게 지도
#     result = 0 # 쓴 사람 수
    
#     for w in weak: # 약점들을 다 지도에 표시 -> 3배 늘어난 지도니까 3번 표시
#         store[w] = 1
#         store[w+n] = 1
#         store[w+(2*n)] = 1
    
#     dist.sort() # 멀리 이동할 수 있는 친구부터 쓰려면 일단 정렬

#     for i in reversed(range(len(dist))): # 정렬했으니까 뒤에서부터 사용
#         friend = dist[i] # 칭구칭구
#         coverages = [] # 이 칭구가 커버할 수 있는 지점의 갯수
#         for w in weak: # 각 약점별로 이거를 이제 해 본다.
#             right = (w + n) + friend # 시계 방향으로 돌기
#             left = (w + n) - friend # 시계 반대 방향으로 돌기

#             if sum(store[w+n:right+1]) >= sum(store[left:w+n+1]): # 시계 방향으로 도는 게 더 효율적이면
#                 coverage = sum(store[w+n:right+1])
#                 coverages.append([coverage, w, 1]) # 그쪽 방향 커버리지로 담아 준다
#             else: # 반대의 경우
#                 coverage = sum(store[left:w+n+1])
#                 coverages.append([coverage, w, -1])

#         coverages.sort(key=lambda x: x[0]) # 가장 높은 커버리지를 가진 쪽으로 갈 수 있게 정렬
#         data = coverages[-1] # 하고 마지막 거 추출
#         starting = data[1] # 시작 약점
#         if data[2] == 1: # 시계 방향
#             store[starting:starting+friend+1] = 0 # 이 범위 내의 원소를 다 0으로 만들어 준다
#         else: # 반시계 방향
#             store[starting-friend:starting+1] = 0
        
#         store = cleaning(store, n) # "클리닝" 해 준다.
#         result += 1 # 사람을 이제 한 명 더 쓴 것
#         if sum(store) == 0: # 더이상 취약한 부분 즉 1이 없으면
#             break # 멈춤
    
#     if sum(store) > 0: # 친구들을 다 동원했는데 아직도 취약점이 있다면
#         return -1 # 실패
    
#     return result # 쓴 친구 동원

# def cleaning(arr, n): # 클리닝 : 배열이 기존 배열의 3배 길이니까, 1구획 2구획 3구획 동기화 필요
#     for i in range(n): # 1구획 0 체크
#         if arr[i] == 0:
#             arr[i+n] = 0
#             arr[i+(2*n)] = 0

#     for i in range(n, (2*n)): # 2구획 0 체크
#         if arr[i] == 0:
#             arr[i-n] = 0
#             arr[i+n] = 0
    
#     for i in range(2*n, len(arr)): # 3구획 0 체크
#         if arr[i] == 0:
#             arr[i-n] = 0
#             arr[i-(2*n)] = 0
    
#     return arr # 체크 후 다 변환한 배열 반환