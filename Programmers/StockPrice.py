# 프로그래머스 코딩테스트 연습 레벨 2 주식 가격
# 참고한 풀이 : https://programmers.co.kr/questions/18569

def solution(prices):
    answer = []
    for i in range(len(prices)): # 가격의 첫 번째 원소부터 순서대로
        for j in range(i+1, len(prices)): # i보다 큰 인덱스를 대상으로
            if prices[i] > prices[j]: # 이는 곧, 가격이 떨어졌다는 얘기.
                break # 해당 조건을 만족하는 j가 나온 시점에서 break
        answer.append(j-i) # 두 인덱스의 차를 answer에 더해 준다. 이는 곧, 소요된 시간을 나타낸다.
    return answer

# 본디 스택/큐 유형의 문제지만, 모로 가도 서울만 가면 된다..
# 시간복잡도를 낮추는 데에는, 1씩 더해주는 부분에 수학적 아이디어를 접목해 한번에 더해주는 것이 일단 도움이 된다.