# def gradingStudents(grades):
#     roundeds = []
#     for grade in (grades):
#
#         if grade >=38:
#             rounded = grade % 5
#             if rounded >= 3:
#                 grade += (5-rounded)
#                 print(grade)
#             else:
#                 print(grade)
#         else:
#             print(grade)
#
#
# grades = [4,73,67,40,33]
# gradingStudents(grades)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 5


def birnary_search_algorithm(list, target):
    list_start = 0
    list_end = len(list) - 1

    while list_start <= list_end:
        mid = (list_start + list_end) // 2
        if target == list[mid]:
            return True

        elif target >= list[mid]:
            list_start = mid + 1


        elif target <= list[mid]:
            list_end = mid - 1

    return False


print(birnary_search_algorithm(list, target))
