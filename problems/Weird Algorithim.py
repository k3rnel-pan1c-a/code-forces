input = int(input())
print(input, end =" ")
while True:
    if input == 1:
        break
    if (input % 2) == 0:
        input = input // 2
        print(input, end =" ")
        if input == 1:
            break
    elif (input % 2) != 0:
        input = (input * 3) + 1
        print(input, end =" ")
        if input == 1:
            break
