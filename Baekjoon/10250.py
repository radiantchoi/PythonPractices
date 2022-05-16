# 백준 온라인 저지 10250번 ACM 호텔

def solution(height, width, number):
    room = 0
    floor = 0

    if number % height == 0:
        room = number // height
        floor = height
    else:
        room = (number // height) + 1
        floor = number % height
        
    return (floor * 100) + room

n = int(input())
for _ in range(n):
    h, w, n = map(int, input().split())
    print(solution(h, w, n))