# 백준 온라인 저지 10809번 알파벳 찾기

# 방법론은 맞는데 왜 안되는지 모르겠는 내 코드
result = [-1] * 26
sentence = input()
for i in range(len(sentence)):
    index = ord(sentence[i]) - 97
    result[index] = i

for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i])
    else:
        print(result[i], end=" ")

# 다른 곳에서 발췌한 코드
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')

# 백준 입력받는건 진짜 극혐인거같음
# 하지만 이 아이디어는 기발한 것 같다
# find는 없으면 알아서 -1을 반환해 준다고 한다. 엄청 신기하다!