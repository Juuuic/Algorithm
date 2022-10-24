n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()

for i in range(n):
    print(data[i])

# 시간초과때문에 input대신에 sys 써야댐
"""
import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)
"""