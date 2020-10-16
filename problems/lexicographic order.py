x, y, z, n = [int(input()) for i in range(4)]
# print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)])
for i in range(0, x + 1):
    for j in range(0, y + 1):
        print([i, j])
