num_cases = int(input())

for _ in range(num_cases):
    count = 1
    string_len, string = [input() for _ in range(2)]
    string_len = int(string_len)
    if string_len == 1:
        print(1)
        continue

    for i in range(1, string_len):
        sub_string = set(string[:i + 1])
        count += len(sub_string)

    print(count)
