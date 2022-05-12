# 백준 온라인 저지 1157번 단어 공부

word = input().upper()
d = {}

for letter in word:
    d[letter] = d.get(letter, 0) + 1

result = []
for key, value in d.items():
    if value == max(d.values()):
        result.append(key)

if len(result) >= 2:
    print("?")
else:
    print(result[0])