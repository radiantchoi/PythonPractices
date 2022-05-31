# 이것이 취업을 위한 코딩 테스트다 p.314 만들 수 없는 금액

n = int(input())
coins = list(map(int, input().split()))

def solution(n, coins):
    result = 1
    prices = set()

    length = 1
    while length <= n:
        for i in range(n-length):
            snippets = coins[i:i+length]
            prices.add(sum(snippets))
        
        length += 1
    
    while result in prices:
        result += 1

    return result

result = solution(n, coins)
print(result)

# 책에 나온 풀이
def solution2(n, coins):
    result = 1
    coins.sort()

    for coin in coins:
        if result < coin:
            break
        result += coin
    
    return result

result2 = solution2(n, coins)
print(result2)