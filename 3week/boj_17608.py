n = int(input())
data = []

for i in range(n):
    x = int(input())
    if i == 0:
        data.append(x)
    else:
        z = data.pop()
        if z < x:
            data.append(x)
        else:
            data.append(z)
            data.append(x)

data = list(set(data))

print(len(data))

# 다시 풀어야댐
