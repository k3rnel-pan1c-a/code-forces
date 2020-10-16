n = int(input())
n2 = [(input()) for i in range(n)]
solved = 0
for i in n2:
    if i.count("0") >= 2 :
        pass
    else:
        solved += 1
print(solved)

