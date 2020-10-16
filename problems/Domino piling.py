input = input().split()
size = int(input[0]) * int(input[1])
while True:
    if size % 2 == 0:
        break
    else:
        size -= 1
print(size//2)