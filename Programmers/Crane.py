# 프로그래머스 코딩테스트 연습 레벨 1 크레인 인형뽑기 게임

# 참고한 풀이 1 : https://velog.io/@matisse/카카오-크레인-인형-뽑기-python
# 참고한 풀이 2 : https://cowimming.tistory.com/52

def solution(board, moves):
    count = 0
    bucket = []
    
    for move in moves:
        for column in board:
            if column[move-1] > 0: # 빈칸이 아니라면
                bucket.append(column[move-1]) # 일단 먼저 바구니에 집어넣고 생각한다
                if len(bucket) > 1: # 그러고 2개 이상 있을 때 중복 여부 체크 (매번 추가할때마다)
                    if bucket[-2] == bucket[-1]: # 끝의 두 개가 같다면?
                        bucket.pop() # del을 써도 되고, 없애는 건 뭘 쓰든 좋다.
                        bucket.pop()
                        count += 2 # "없어진 인형의 갯수"
                
                column[move-1] = 0 # 뽑은 인형 자리를 0으로 만들어 준다
                break # 인형을 하나 뽑았으므로 루프를 멈춰 줘야 한다.
                # moves에서 같은 숫자가 여러 번 나오는 거 봤지? 그 줄에 용건이 있으면 또 들어온다는 말이다.
                # 해당 줄에서 한번에 인형을 다 뽑을 게 아니고, 하나씩 뽑을 거기 때문에, break를 걸어 줘야 한다.
                    
    return count

# 세로로 긴 통을 생각했지만, 사실 2차원 리스트의 구조를 생각해보면 세로 * 가로가 좀 더 옳은 표현
# 또한 마이너스 인덱스를 활용하는 데 거부감을 없애야 한다.