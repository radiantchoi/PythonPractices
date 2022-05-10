# 백준 온라인 저지 8958번 OX퀴즈

n = int(input())

for _ in range(n):
    board = input()
    score = 0
    streak = 0
    
    for i in range(len(board)):
        if board[i] == "O":
            streak += 1
            score += streak
        else:
            streak = 0
    
    print(score)

