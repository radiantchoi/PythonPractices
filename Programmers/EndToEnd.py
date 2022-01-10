# 프로그래머스 코딩테스트 연습 레벨 2 영어 끝말잇기
# 참고한 풀이 : https://programmers.co.kr/questions/7023

def solution(n, words):
    answer = [0, 0]
    # 사람 번호 : 인덱스 나누기 n의 나머지 + 1
    # 차례 번호 : 인덱스를 n으로 나눈 몫 + 1
    # 탈락 : 끝말잇기가 아니게 될 경우 / 중복 단어가 나올 경우
    
    storage = []
    storage.append(words[0])
    
    for i in range(1, len(words)):
        storage.append(words[i])
        if storage[-2][-1] != storage[-1][0]:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break
        if storage[-1] in storage[:len(storage)-1]:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break

    return answer

# for문은 뒤에서부터 훑는 것 같다. 상기 링크의 첫 번째 테스트 케이스에서 [2, 2]가 아닌 [1, 3]이 자꾸 나왔다.
# 그래서 아예 단어를 리스트 안에 넣고, 리스트 안에 있는 단어끼리만 비교했다.
# 이렇게 함으로써 아직 공식적으로 개입하지 않았어야 하는 단어를 배제하고 비교할 수 있었다.
# 원래는 별도의 storage를 지정하지 않고 words 리스트 안에서 직접 비교했었다.
# 정작 차례 번호 구하는 걸 헷갈릴 뻔했지만 잘 구했다..