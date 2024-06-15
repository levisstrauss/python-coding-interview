# Brute force

# def target(array, target):
#     for p1 in range(len(array) - 1):
#         number = target - array[p1]
#         for p2 in range(p1 + 1, len(array)):
#             if number == array[p2]:
#                 return [p1, p2]
#     return False


# test = [4, 123, 6, 7]
#
# print(target(test, 10))


def target(array, target):
    left, right = 0, len(array) - 1

    while left < right:
        result = array[left] + array[right]
        if result == target:
            return [left, right]
        elif result < target:
            left = left + 1
        else:
            right = right - 1
    return False


test = [4, 123, 6, 7]

print(target(test, 10))
