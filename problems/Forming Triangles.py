num_cases = int(input())

for _ in range(num_cases):
    string_len, string = [input().split() if i == 1 else int(input()) for i in range(2)]
    ans = 0
    if string_len < 3:
        print(0)
        continue

    num_lengths = {int(i): 0 for i in string}
    for i in range(string_len):
        num_lengths[int(string[i])] += 1

    num_lengths = dict(sorted(num_lengths.items()))
    sum = 0

    for length, count in num_lengths.items():
        if count >= 3:
            ans += count * (count - 1) * (count - 2) // 6

        if count >= 2:
            ans += count * (count - 1) // 2 * sum

        sum += count

    print(ans)

