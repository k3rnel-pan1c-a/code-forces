num_cases = int(input())

for _ in range(num_cases):
    count = 0
    string_len, string = [input() for _ in range(2)]
    string_len = int(string_len)
    if string_len == 1:
        print(1)
        continue
    distinct = set()
    for i in range(0, string_len):
        distinct.add(string[i])
        count += len(distinct)

    print(count)
