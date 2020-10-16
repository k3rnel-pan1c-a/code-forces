n = list(input())
count = 0
max = 0
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        count += 1
        if max <= count:
            max = count
    elif n[i] != n[i+1]:
        count = 0
print(max+1)

