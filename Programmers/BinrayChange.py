# 프로그래머스 코딩테스트 연습 레벨 2 이진 변환 반복하기
# 참고한 풀이 : https://programmers.co.kr/questions/15195

def solution(s):
    count = 0
    change = 0
    
    while s != "1":
        digits = list(s)
        zero = 0
        for i in range(len(digits)):
            if digits[i] == "0":
                zero += 1
                count += 1
        s = bin(len(digits)-zero)[2:]
        change += 1
            
    return [change, count]

# 처음에는 리스트에서 하나하나 remove했지만, 그것보다 그냥 0의 갯수를 세고 그거만큼 길이에서 빼 주는 게 나았다.
# 리스트 요소를 건드리는 것 자체가 시간복잡도를 꽤 많이 잡아먹고, for보다 while이 그런 함정에 빠지기 쉬우니만큼..
# 최상단 while의 조건을 "1"이 아니라 1로 적어서, 계속 무한루프에 빠졌었다. 실수하지 말자.