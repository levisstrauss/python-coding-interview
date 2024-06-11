"""
In this problem, we want to see if by removing one character in either left
or right, the given string can be a palindrome
"""


# This function check if  the given word is a palindrome
def two_pointers(array, left, right):
    # This function checks if the subarray from index `left` to `right` is a palindrome.
    while left < right:
        # If the characters at the current left and right pointers do not match, return False.
        if array[left] != array[right]:
            return False
        # Move the left pointer one step to the right.
        left += 1
        # Move the right pointer one step to the left.
        right -= 1
    # If all characters matched, return True indicating the subarray is a palindrome.
    return True


def is_palindrome(s: str) -> bool:
    # Convert the input string `s` into a list of characters `s_arr`.
    s_arr = list(s)
    # Initialize two pointers: `left` starting at the beginning of the list,
    # and `right` starting at the end of the list.
    left, right = 0, len(s_arr) - 1

    # Traverse the list from both ends towards the center.
    while left < right:
        # If characters at the left and right pointers do not match:
        if s_arr[left] != s_arr[right]:
            # Check if the subarray obtained by skipping the character at `left` is a palindrome.
            skip_left = two_pointers(s_arr, left + 1, right)
            # Check if the subarray obtained by skipping the character at `right` is a palindrome.
            skip_right = two_pointers(s_arr, left, right - 1)
            # If either of the above checks return True, the string can be made a palindrome
            # by removing at most one character.
            return skip_left or skip_right
        # If characters match, move both pointers towards the center.
        left += 1
        right -= 1

    # If the entire list is traversed without needing to remove more than one character,
    # return True indicating the string is already a palindrome or can be made one by
    # removing at most one character.
    return True


# Example usage:
s = "madame"
print(is_palindrome(s))  # Output: False
