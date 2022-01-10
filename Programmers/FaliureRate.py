# 프로그래머스 코딩테스트 연습 레벨 1 실패율

def solution(N, stages):

    # stages의 원소 = 현재 해당 스테이지 도전 중(도달했으나 클리어하지 못한 사람. 단, N+1이면 전체 클리어를 한 사람)
    # 실패율 = 해당 스테이지를 아직 못 깬 사람 / 해당 스테이지에 도달한 사람
    # 1에서 N까지의 범위 내에서 (stages의 원소가 같은 사람 / stages의 원소가 크거나 같은 사람) 이게 스테이지별 실패율
    # 해결 방법 : 각 스테이지 번호를 키, 실패율을 밸류로 삼는 딕셔너리를 만들고, 내림차순으로 정렬하고, 키만 뽑아서 answer에 더한 다음 출력

    failrate = [2.0] # 인덱스 번호를 스테이지로 만들기 위해, 0에 해당하는 부분을 확률에서 나올 수 없는 2.0으로 채워놓음

    for m in range(1, N+1):
        wasstage = 0
        onstage = 0
        for i in stages:
            if i >= m:
                wasstage += 1
                if i == m:
                    onstage += 1
        if wasstage == 0: # division by zero 방지용. 아직 도달한 사람이 없다는 뜻이니까
            failrate.append(0) # 문제에서 제시한 0으로 바꿔 주었다
        else:
            failrate.append(onstage / wasstage)

    ratetable = {}
    for n in range(1, len(failrate)):
        ratetable[n] = failrate[n] # 딕셔너리에 스테이지별 실패율 요소 추가

    # 값을 기준으로 내림차순 정렬
    # 딕셔너리에서 해당 값이 있는 위치의 키를 answer 리스트에 더하기

    sorting = sorted(ratetable.items(), key = lambda x: x[1], reverse = True) # 오늘의 몰랐던 부분

    answer = []
    for j in range(len(sorting)):
        answer.append(sorting[j][0])

    return answer

# 알아둘 것 : 딕셔너리 정렬하기, 딕셔너리 만들기(중괄호로 만들어야 함)