n = int(input())
list = [int(i) for i in input().split()]
Turns = 0
for i in range(n-1):
    if list[i] > list[i+1]:
        Turns += list[i] - list[i+1]
        list[i+1] = list[i]

print(Turns)
