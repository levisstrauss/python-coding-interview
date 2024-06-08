"""
Given an array, how to reverse that array using two pointer

"""


def reverse_array(array):
    left, right = 0, len(array) - 1
    while left < right:
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        return array


array = [2, 4, 5]

print(reverse_array(array))
