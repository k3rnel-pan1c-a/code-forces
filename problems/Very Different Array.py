num_cases = int((input()))

for _ in range(num_cases):
    arrays_lens, array_a, array_c = [input().split() for _ in range(3)]
    if arrays_lens[0] == '1':
        print(max(list(map(int, array_c))) - int(array_a[0]))
        continue
    diff = 0
    even_len = False

    array_c_ascending = sorted(list(map(int, array_c)))
    array_a_descending = sorted(list(map(int, array_a)), reverse=True)

    if int(arrays_lens[0]) % 2 == 0:
        even_len = True

    if even_len:
        mid_point = int(arrays_lens[0]) // 2 - 1
    else:
        mid_point = int(arrays_lens[0]) // 2

    count = 0
    for i in range(int(arrays_lens[0])):

        if i <= mid_point:
            diff += abs(array_a_descending[i] - array_c_ascending[count])
            count += 1
            if i == mid_point:
                count = 0

        else:
            diff += abs(array_c_ascending[int(arrays_lens[1]) - 1 - count] - array_a_descending[i])
            count += 1

    print(diff)
