# 백준 온라인 저지 4344번 평균은 넘겠지

n = int(input())

for _ in range(n):
    data = list(map(int, input().split()))
    people = data[0]
    scores = data[1:]
    avg = sum(scores) / people

    app = 0
    for score in scores:
        if score > avg:
            app += 1
    
    result = round(app / people * 100, 3)
    print("%.3f" % result+"%")

# 포매팅 함수 쓰라는건가?
# 이걸 안썼다고 틀림 판정 뜨는게 말이 안된다 진짜 개때리고싶음