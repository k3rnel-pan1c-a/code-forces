num_cases = int(input())


def valid_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x


for _ in range(num_cases):
    string_len, string = [input().split() if i == 1 else int(input()) for i in range(2)]
    ans = 0
    if string_len == 1:
        print(0)
        continue
    num_lengths = {i: 0 for i in string}
    for i in range(string_len):
        num_lengths[string[i]] += 1

    for length, count in num_lengths.items():
        if count >= 3:
            ans += count * (count - 1) * (count - 2) // 6

        if count >= 2:
            ans += count * (count - 1) // 2 * (string_len - count)

    print(ans)

