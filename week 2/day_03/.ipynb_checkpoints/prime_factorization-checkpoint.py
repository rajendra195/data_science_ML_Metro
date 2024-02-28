num = 36
l = []

for i in range(2, 22):
    for j in range(2, 22):
        if i * j == num:
            print(i, j)
k = set(l)
print(l)
print(k)