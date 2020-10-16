n = list(map(int,input().split()))
a = n[2]
b= n[0]
c= n[1]
m= (b // a)
n= (c // a)
if (b % a) != 0:
    m += 1
if (c % a) != 0:
    n += 1
print(n*m)