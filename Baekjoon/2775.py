# 백준 온라인 저지 2775번 부녀회장이 될테야

n = int(input())

def solution(floor, room):
    # 주어진 층, 주어진 호수까지만 아파트를 만들어주면 되지!
    ground = [x for x in range(room+1)]
    apt = [ground]

    for _ in range(1, floor+1):
        newfloor = [0]
        for j in range(1, room+1):
            newfloor.append(apt[-1][j] + newfloor[-1])
        
        apt.append(newfloor)
    
    return apt[-1][-1]

for _ in range(n):
    floor = int(input())
    room = int(input())
    print(solution(floor, room))