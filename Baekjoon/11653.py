# 백준 온라인 저지 11653번 소인수분해

n = int(input())
for number in range(2, n+1):
    if number > n:
        break

    while n % number == 0:
        n /= number
        print(number)

# 참조 : https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-11653%EB%B2%88-%EC%86%8C%EC%9D%B8%EC%88%98%EB%B6%84%ED%95%B4-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC