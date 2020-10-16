n = [input().split() for i in range(5)]
operations = 0
for i in range(len(n)):
    for index,item in enumerate(n[i]):
       if int(item) == 1:
            if index > 2:
                operations += (index-2)
            elif index < 2:
                operations += (2-index)
            if i > 2:
                operations += (i-2)
            elif i < 2:
                operations += (2-i)
print(operations)