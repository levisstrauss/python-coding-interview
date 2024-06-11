"""
Given an array of positive numbers, nums, such that the values lie in the range
[1,𝑛], inclusive, and that there are 𝑛+1
numbers in the array, find and return the duplicate number present in nums. There is only one repeated number in nums.

"""

"""
Complexity O(n)

Space O(1)

"""


def find_duplicate(nums):
    # Initialize the fast and slow pointers and make them point the first
    # element of the array
    fast = slow = nums[0]
    # PART #1
    # Traverse in array until the intersection point is found
    while True:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # Move the fast pointer two times fast as the slow pointer using the
        # nums[nums[fast]] flow
        fast = nums[nums[fast]]
        # Break the loop when slow pointer becomes equal to the fast pointer, i.e.,
        # if the intersection is found
        if slow == fast:
            break
    # PART #2
    # Make the slow pointer point the starting position of an array again, i.e.,
    # start the slow pointer from starting position
    slow = nums[0]
    # Traverse in the array until the slow pointer becomes equal to the
    # fast pointer
    while slow != fast:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # Move the fast pointer slower than before, i.e., move the fast pointer
        # using the nums[fast] flow
        fast = nums[fast]
    # Return the fast pointer as it points the duplicate number of the array
    return fast


# Driver code
def main():
    nums = [
        [1, 3, 2, 3, 5, 4],
        [2, 4, 5, 4, 1, 3],
        [1, 6, 3, 5, 1, 2, 7, 4],
        [1, 2, 2, 4, 3],
        [3, 1, 3, 5, 6, 4, 2]
    ]
    for i in range(len(nums)):
        print(i + 1, ".\tnums = ", nums[i], sep="")
        print("\tDuplicate number = ", find_duplicate(nums[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
