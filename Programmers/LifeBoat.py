# 프로그래머스 코딩테스트 연습 그리디 레벨 2 구명보트

# 참고한 풀이 : https://leedakyeong.tistory.com/entry/프로그래머스-구명보트-in-python

def solution(people, limit):
    count = 0
    people.sort() # 그리디 문제는 정렬을 염두에 둬 보자. "가장" 의 조건을 충족시키기 쉽기 때문
    firstIndex = 0; lastIndex = len(people) - 1 # 정렬되어 있으므로, 처음 원소는 가장 가볍고 마지막 원소는 가장 무겁다
    while firstIndex <= lastIndex: # 둘이 어긋나는 순간 반복문이 끝난다. 
        count += 1 # 일단 보트 하나 추가. 어차피 누군가는 태울 테니까
        if people[firstIndex] + people[lastIndex] <= limit: # 둘이 합쳐서 리미트에 도달하지 않는 경우에만~
            firstIndex += 1 # 이전 인덱스의 사람을 태웠다고 가정하고 가벼움 인덱스를 올린다. 즉 두 명이 탄 것
        lastIndex -= 1 # 무거움 인덱스는, 어쨌든 보트 하나를 차지하기 때문에 태웠다고 가정하고 다음 무거운 사람으로 넘어간다.
    return count

# 리스트 인덱싱이 아닌, 실제 리스트의 요소를 건드리면 효율성 테스트에서 탈락한다고 한다. 최대 O(n)이라서 그런 듯
# 컴퓨터적 사고방식을 훈련해야 하며, 그것을 위해 알고리즘 연습을 단단히 해야 할 것 같다
