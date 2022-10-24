n = int(input())
data = list(map(int, input().split()))
k = int(input())

d1 = sorted(data[:n//k])
d2 = sorted(data[n//k:])

print(*d1, *d2)

#다시 풀기