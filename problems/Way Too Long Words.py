n = int(input())
n2 = [(input()) for i in range(n)]
for i in n2:
    if len(i) > 10:
        print(i[0]+str(len(i)-2)+i[-1])
    else:
        print(i)