n = list(input())
dist_chars = 0
count = 0
n.sort()
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        dist_chars += 1
if (dist_chars+1) % 2 ==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
