"""
 Whatever there is a need of finding two data,
 Naive approach: nested loops -> O(n^2)
 Better approach: Two pointer -> O(n)

Note: A palindrome is a word, phrase, or sequence of
      characters that reads the same backward as forward.

How to solve this problem:

- Initialize p1 and p2
- Check if: p1 = p2
- if p1 # p2 return false, otherwise p1.index = 1 and p2.index = 1
- Traverse until middle
- if middle not finding mismatch, return True
"""

"""
Simple way of traversing and reversing a string 
 
 - word[::-1]
 - ".join(reversed("test")
 - using for loop
   reverse_test = ""
   for char in word:
     reverse_test = char + reversed_str
    

"""

print(''.join(reversed("test")))


# Naive approach
# def is_palindrome(word: str) -> bool:
#     reverse_word = word[::-1]
#     if reverse_word != word:
#         return False
#     return True


def is_palindrome(word: str) -> bool:
    # Initialization
    left, right = 0, len(word) - 1
    # Check for the middle
    while left < right:
        # Compare them
        if word[left] != word[right]:
            return False
        # Increment them
        left, right = left + 1, right - 1
    return True


print(is_palindrome("abba"))  # True
print(is_palindrome("abbas"))  # False
