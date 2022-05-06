# 프로그래머스 코딩테스트 연습 레벨 2 k진수에서 소수 개수 구하기

from math import sqrt

def solution(n, k):
    
    def jinsu(n, k):
        result = ""
        while n > 0:
            n, mod = divmod(n, k)
            result += str(mod)
        
        return result[::-1]
        
    def isPrime(n):
        if n in range(0, 2):
            return False
        elif n == 2:
            return True
        
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        
        return True
    
    rawdata = jinsu(n, k)
    datas = rawdata.split("0")
    numbers = [x for x in datas if x != "" and isPrime(int(x))]
    
    return len(numbers)

# 기록 : https://velog.io/@radiantchoi/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.2-k%EC%A7%84%EC%88%98%EC%97%90%EC%84%9C-%EC%86%8C%EC%88%98-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0-T