n = 5
data = [10, 20, 30, 40, 50]

value = 0
sums = [0]
for n in data:
    value += n
    sums.append(value)

# left부터 right까지 구간의 합을 알고 싶다면
right = 4
left = 3
print(sums[right] - sums[left - 1])