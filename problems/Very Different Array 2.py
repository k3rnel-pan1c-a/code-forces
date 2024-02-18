num_cases = int((input()))

for _ in range(num_cases):
    arrays_lens, array_a, array_c = [input().split() for _ in range(3)]

    array_c = sorted(list(map(int, array_c)))
    array_a = sorted(list(map(int, array_a)), reverse=True)

    total_diff = 0

    for _ in range(int(arrays_lens[0])):
        c_max = array_c[-1]
        c_min = array_c[0]

        a_max = array_a[0]
        a_min = array_a[-1]

        if abs(a_max - c_min) > abs(c_max - a_min):
            total_diff += abs(a_max - c_min)
            array_c.pop(0)
            array_a.pop(0)
        else:
            total_diff += abs(c_max - a_min)
            array_c.pop(-1)
            array_a.pop(-1)

    print(total_diff)
