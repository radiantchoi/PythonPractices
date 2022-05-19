# 백준 온라인 저지 10872번 팩토리얼

def factorial(n):
    if n < 2:
        return 1
    
    return n * factorial(n-1)

n = int(input())
print(factorial(n))