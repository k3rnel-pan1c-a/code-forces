n = list(input())

for i in range(len(n)):
    if n[i] % 2 == 0:
        if n[i+1] % 2 !=0:
            n[i+1] = n[i]
    else:
        print("NO SOLUTION")