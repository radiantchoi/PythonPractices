# 프로그래머스 코딩테스트 연습 레벨 2 소수 찾기

import itertools
import math

def isprime(n):
    result = True

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            result = False

    return result

def solution(numbers):
    digits = list(numbers)
    picked = []
    chunks = []
    nums = []
    count = 0

    for n in range(1, len(digits)+1):
        picked += list(itertools.permutations(digits, n))

    for cards in picked:
        chunks.append(list(cards))

    for num in chunks:
        nums.append(int("".join(num)))

    numset = set(nums)
    nums = list(numset)

    for num in nums:
        if num > 1 and isprime(num) == True:
            count += 1

    return count

# 멀리멀리 돌아서 결국 풀어냈는데, 여러 라이브러리 사용법을 더 익혀둬야겠다고 생각했다.
# 셋과 리스트, 퍼뮤테이션까지 여러 자료형을 오가는 것도 꽤 괜찮은 것 같다.