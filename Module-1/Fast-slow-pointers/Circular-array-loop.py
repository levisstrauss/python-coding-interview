# def circular_array_loop(nums):
#     # Inner function to calculate the next index
#     def next_step(i):
#         return (i + nums[i]) % len(nums)
#
#     # Iterate through each index of the array
#     for i in range(len(nums)):
#         # If the current element is 0, it means it has been visited and can be skipped
#         if nums[i] == 0:
#             continue
#
#         # Initialize slow and fast pointers to the current index
#         slow, fast = i, i
#
#         # Loop to move the slow and fast pointers to detect cycles
#         # Check that the direction remains the same and that the next step is not zero
#         while nums[slow] * nums[next_step(slow)] > 0 and nums[fast] * nums[next_step(fast)] > 0 and nums[fast] * nums[next_step(next_step(fast))] > 0:
#             slow = next_step(slow)  # Move slow pointer one step
#             fast = next_step(next_step(fast))  # Move fast pointer two steps
#
#             # If slow and fast pointers meet, check for a valid cycle
#             if slow == fast:
#                 # Check for a single-element cycle
#                 if slow == next_step(slow):
#                     break
#                 return True
#
#         # If no cycle is found, mark the path as visited
#         marker = i
#         while nums[marker] * nums[next_step(marker)] > 0:
#             next_marker = next_step(marker)  # Calculate the next index
#             nums[marker] = 0  # Mark the current index as visited
#             marker = next_marker  # Move to the next index
#
#     # If no cycle is found in the entire array, return False
#     return False

"""


Time complexity: O(n^2)

Space O(1)
"""




def circular_array_loop(nums):
    # Inner function to calculate the next index
    def next_step(i):
        return (i + nums[i]) % len(nums)

    # Iterate through each index of the array
    for i in range(len(nums)):
        # If the current element is 0, it means it has been visited and can be skipped
        if nums[i] == 0:
            continue

        # Initialize slow and fast pointers to the current index
        slow, fast = i, i

        # Loop to move the slow and fast pointers to detect cycles
        # Check that the direction remains the same and that the next step is not zero
        while nums[slow] * nums[next_step(slow)] > 0 and nums[fast] * nums[next_step(fast)] > 0 and nums[fast] * nums[next_step(next_step(fast))] > 0:
            slow = next_step(slow)  # Move slow pointer one step
            fast = next_step(next_step(fast))  # Move fast pointer two steps

            # If slow and fast pointers meet, check for a valid cycle
            if slow == fast:
                # Check for a single-element cycle
                if slow == next_step(slow):
                    break
                return True

        # If no cycle is found, mark the path as visited
        marker = i
        while nums[marker] * nums[next_step(marker)] > 0:
            next_marker = next_step(marker)  # Calculate the next index
            nums[marker] = 0  # Mark the current index as visited
            marker = next_marker  # Move to the next index

    # If no cycle is found in the entire array, return False
    return False