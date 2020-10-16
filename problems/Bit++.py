x = 0
n = int(input())
n2 = [(input()) for i in range(n)]
for i in n2:
    if '+' in i:
        x += 1
    elif '-' in i:
        x -= 1
print(x)