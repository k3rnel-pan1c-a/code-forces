n= list(map(int,input().split()))
years = 0
while True:
    years +=1
    n[0] = n[0] * 3
    n[1] = n[1] * 2
    if n[0] > n[1]:
        break
print(years)