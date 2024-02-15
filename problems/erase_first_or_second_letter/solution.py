with open("input.txt", "r") as f:
    lines = f.readlines()


def remove_first_second_char(sub_strings: set, string: str):
    if len(string) == 1:
        sub_strings.add(string)
        return

    for idx in range(2):
        if idx == 0:
            sub_strings.add(string[1:])
            remove_first_second_char(sub_strings, string[1:])
        else:
            sub_strings.add(string[:1] + string[2:])
            remove_first_second_char(sub_strings, string[:1] + string[2:])


sub_strings = set()
remove_first_second_char(sub_strings, "ababa")  # Test Case

print(len(sub_strings) + 1)  # Addition of one in case of doing no operations
