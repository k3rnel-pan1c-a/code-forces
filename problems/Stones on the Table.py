n = int(input())
n2 = list(input())
count = 0
for i in range(len(n2)-1):
    if n2[i] == n2[i+1]:
        count += 1

print(count)