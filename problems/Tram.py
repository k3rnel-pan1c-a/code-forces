list1= []
n1 = int(input())
for i in range(n1):
    list1.append(list(map(int,input().split())))
passengers = 0
min_capacity = []
for i in list1:
    passengers -= i[0]
    passengers += i[1]
    min_capacity.append(passengers)
min_capacity.sort(reverse=True)
print(min_capacity[0])





