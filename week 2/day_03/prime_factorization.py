num = 36
l = []

for i in range(2, 22):
    for j in range(2, 22):
        if i * j == num:
            l.append(i)
            l.append(j)
k = set(l)
print(l)
print(k)