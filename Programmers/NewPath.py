# 프로그래머스 코딩테스트 연습 레벨 2 방문 길이
# 참고한 풀이 : https://programmers.co.kr/questions/12535

def solution(dirs):
    answer = 0
    move = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    logs = set()
    x = 0
    y = 0
    
    for d in dirs:
        dx, dy = move[d] # 깔끔한 처리
        nx = x + dx
        ny = y + dy
        
        if nx <= 5 and ny <= 5 and nx >= -5 and ny >= -5:
            ff = (x, y, nx, ny)
            rew = (nx, ny, x, y)
            x = nx
            y = ny
            
            if ff not in logs:
                logs.add(ff)
                logs.add(rew)
                answer += 1
            
    return answer

# 아이디어는 있지만, 파이썬에 익숙하지 않다는 것을 적나라하게 드러낸 문제였다.
# 경로가 중복되지 않아야 한다는 아이디어는 좋았고, 로그 리스트 지정 후 마지막에 not in을 사용했다.
# 하지만, 알 수 없는 오류로 케이스 통과를 못 했다.
# 차라리 예시처럼 로그를 집합으로 만들어 중복을 회피하는 게 좋았다.
# 그리고 나서 x,y와 nx,ny를 활용한 정방향 역방향 좌표로 하여금 경로를 나타내고, 이것의 중복 여부를 체크하는 것이다.
# move를 딕셔너리로 나타낸 것 또한 깔끔하다고 느꼈다. 튜플의 원소를 변수에 넣을 수 있다는 것도 배웠다.
# 또한 좌표의 갱신 및 경로의 생성 또한 명령이 실행되어야 실행되는 것이므로, 좌표평면을 벗어나는 명령은 무시하게끔 짜야 한다.
# 구현 중 시뮬레이션 문제는 x와 y 좌표를 설정하고 푸는 것이 좋다고 느꼈다.
