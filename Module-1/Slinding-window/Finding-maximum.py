"""
Given an integer list, nums, find the maximum values in all the contiguous
 subarrays (windows) of size w.
"""

from collections import deque

def clean_up(i, current_window, nums):
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()

def find_max_sliding_window(nums, w):
    if len(nums) == 1:
        return nums

    output = []
    current_window = deque()

    # Initialize the deque for the first window
    for i in range(w):
        clean_up(i, current_window, nums)
        current_window.append(i)

    # Add the maximum for the first window
    output.append(nums[current_window[0]])

    # Process the rest of the windows
    for i in range(w, len(nums)):
        clean_up(i, current_window, nums)

        # Remove the elements not within the current window
        if current_window and current_window[0] <= i - w:
            current_window.popleft()

        current_window.append(i)
        output.append(nums[current_window[0]])

    return output
