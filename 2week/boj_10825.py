n = int(input())
data = [0] * n

for i in range(n):
    name, a, b, c = map(str, input().split())
    data[i] = (name, int(a), int(b), int(c))

"""
for i in range(n-1):
    if data[i][1] < data[i+1][1]:
        d = data[i]
        data[i] = data[i+1]
        data[i+1] = d
    elif data[i][1] == data[i+1][1]:
        if data[i][2] > data[i+1][2]:
            t = data[i]
            data[i] = data[i+1]
            data[i+1] = t
        elif data[i][2] == data[i+1][2]:
            if data[i][3] < data[i+1][3]:
                y = data[i]
                data[i] = data[i+1]
                data[i+1] = y
            elif data[i][3] == data[i+1][3]:
                if data[i][0] > data[i+1][0]:
                    p = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = p




d1 = sorted(data, key=lambda x: (x[1]), reverse=True)
d2 = sorted(d1, key=lambda x: (x[2]))
d3 = sorted(d2, key=lambda x: (x[3]), reverse=True)
d4 = sorted(d3, key=lambda x: (x[0]))
"""

data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(data[i][0])
