# 이것이 취업을 위한 코딩 테스트다 p.217 1로 만들기

x = int(input())

def solution(x):
    result = 0

    table = {0: [x]}
    while True:
        new = []
        for n in table[result]:
            if n % 5 == 0:
                new.append(n / 5)
            if n % 3 == 0:
                new.append(n / 3)
            if n % 2 == 0:
                new.append(n / 2)
            new.append(n - 1)
        
        result += 1
        if 1 in new:
            break
        else:
            table[result] = new

    return result

print(solution(x))

# 책에 써 있는 거랑 방법론은 완전 다르긴 한데, 답은 잘 나온다.