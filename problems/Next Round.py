n = input().split()
n2 = input().split()
count = 0
for index, item in enumerate(n2):
    if int(item) != 0:
        if int(item) >= int(n2[int(n[1])-1]):
            count += 1
    else:
        pass

print(count)