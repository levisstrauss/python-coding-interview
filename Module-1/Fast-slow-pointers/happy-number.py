"""

Write an algorithm to determine if a number
𝑛 is a happy number.

We use the following process to check if a given number is a happy number:

Starting with the given number 𝑛
, replace the number with the sum of the squares of its digits.
Repeat the process until:
The number equals
1, which will depict that the given number
𝑛 is a happy number.
The number enters a cycle, which will depict that the given number
𝑛, is not a happy number.
Return TRUE if
𝑛, is a happy number, and FALSE if not.

"""

# Thought process

"""
1- set two  pointers slow -> points to the input number
 fast -> points to the sum of squared digits of the input number
 
2 - Start a loop until fast reaches 1 of both meet indicating a cycle

3- Update the slow by adding the squares of its digits and fast by adding
the squares of its digits twice

4- If fast == 1 return true otherwise False

"""

#
# def is_happy_number(n):
#     def sum_of_squares(num):
#         return sum(int(digit) ** 2 for digit in str(num))
#
#     seen = set()
#
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = sum_of_squares(n)
#
#     return n == 1


"""
Time complexity: O(log n) where n is the input number

"""


def is_happy_number(n):
    # Helper function that calculates the sum of squared digits.
    def sum_of_squared_digits(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_pointer = n
    fast_pointer = sum_of_squared_digits(n)

    while fast_pointer != 1 and slow_pointer != fast_pointer:
        slow_pointer = sum_of_squared_digits(slow_pointer)
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))

    if fast_pointer == 1:
        return True
    return False


def main():
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(i + 1, ".\tInput Number: ", inputs[i], sep="")
        print("\n\tIs it a happy number? ", is_happy_number(inputs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
