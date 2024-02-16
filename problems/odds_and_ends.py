sequence_len, sequence = [input().split() if i == 1 else input() for i in range(2)]
if int(sequence[0]) % 2 == 1 and int(sequence[-1]) % 2 == 1 and int(sequence_len) % 2 == 1:
    print("Yes")
else:
    print("No")




