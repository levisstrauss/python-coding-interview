"""

Thought Process:

1- sort the array first in ascending order
2- create two pointers low and high
3 - put low at index i + 1 and high at index len(string) -1
4 - for i in range(0, len(string) - 2 because high is already at the last index
5 - triplet = string[i] + string[low] + string[high]
6 - if triplet == target return True
7 - elif triplet < target,then push low to the front otherwise decrease high
8 - if the number is not found then return False
"""

"""

Time complexity 
 For the two nested loop: 
 sorting the array is O(nlog n) the nested loop take O(n^2)
We have O(nlog n + n^2) = n^2


Space complexity O(n) because of the builtin function
"""


# Code
def find_sum_of_three(nums, target):
    # Sort the input list
    nums.sort()

    # Fix one integer at a time and find the other two
    for i in range(0, len(nums) - 2):
        # Initialize the two pointers
        low = i + 1
        high = len(nums) - 1

        # Traverse the list to find the triplet whose sum equals the target
        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            # The sum of the triplet equals the target
            if triplet == target:
                return True

            # The sum of the triplet is less than target, so move the low pointer forward
            elif triplet < target:
                low += 1

            # The sum of the triplet is greater than target, so move the high pointer backward
            else:
                high -= 1

    # No such triplet found whose sum equals the given target
    return False


# Driver code
def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-" * 100)


if __name__ == '__main__':
    main()

