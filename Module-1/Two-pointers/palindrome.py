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

# Naive approach
# def is_palindrome(word: str) -> bool:
#     reverse_word = word[::-1]
#     if reverse_word != word:
#         return False
#     return True

"""
The time complexity is O(n), where 𝑛 is the number of characters in the string. 
However, our algorithm will only run (n/2) times, since two pointers are traversing
 toward each other.
 
 space  complexity is O(1) since we use constant space to store two indexs
"""


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True


# Driver Code
def main():
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".",
              sep='')
        print("Is it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)
