# 이것이 취업을 위한 코딩 테스트다 p.226 효율적인 화폐 구성

n, m = map(int, input().split())
c = []
for _ in range(n):
    c.append(int(input()))

def solution(target, coins):
    result = -1

    table = {0: set([0])}
    table[1] = set(coins)

    number = 1
    while True:
        new = []
        for price in table[number]:
            for coin in coins:
                new.append(price + coin)
        
        number += 1
        if target in new:
            result = number
            break
        else:
            new.sort()
            if target < new[0]:
                break
            else:
                table[number] = set(new)

    return result

print(solution(m, c))

# 동적 계획법도 장착!
# 탈출 조건에 대해 깊이 생각해보자.