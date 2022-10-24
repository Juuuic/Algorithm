n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
i = 0
answer = 0
first = data[n-1]
second = data[n-2]

while True:
    for _ in range(k):
        answer += first
        i += 1
        if i == m:
            break

    answer += second
    i += 1
    if i == m:
        break


print(answer)