# 이것이 취업을 위한 코딩 테스트다 p.361 실패율
# 프로그래머스 주소 : https://programmers.co.kr/learn/courses/30/lessons/42889
# 제한시간 20분

# 1회차 실패 - 아니 시발 시간초과가 왜 뜨지 도대체??
# 아무래도, 최대한 체크할 것을 줄이는 것이 좋겠다.
# 클리어한 사람까지 카운팅할 필요는 없고, 지금 스테이지에 있는 인원 / 지금까지의 총 인원 하면 실패율이 나온다.
# 이 스테이지에 있지 않으면서 지금까지의 총 인원에 포함된다는 것은, 이 스테이지를 깼다는 거니까.

# 1회차의 실패한 솔루션
def solutionfalied(N, stages):
    failrate = {}
    reached = {}
    cleared = {}
    for i in range(1, N+1):
        reached[i] = 0
        cleared[i] = 0
        failrate[i] = 0

    for user in stages:
        for i in range(1, user):
            cleared[i] += 1
            reached[i] += 1
        
        if user > N:
            continue
        else:
            reached[user] += 1

    for i in range(1, N+1):
        r = reached[i]
        c = cleared[i]

        if r == 0:
            continue
        else:
            failrate[i] = (r - c) / r
        
    result = [x for x in range(1, N+1)]
    result.sort(key = lambda x: (-failrate[x], x))
    return result