"""
Given an array, colors, which contains a combination of the following three elements:
 - 0 red
 - 1 white
 - 2 blue

Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue.
To improve your problem-solving skills, do not utilize the built-in sort function.
"""

# Thought process
"""
1
    declare three pointers
    start = 0
    current = 0
    end = len(colors) - 1
    
2 
  if color[current] is 0, swap it value with colors[start]
  and increment both the current and start
3
  Otherwise, if colors[current] is 1, just increment the current
  otherwise colors[current] will be 2 so swap its value with colors[end]
  and decrement end
  
4 
 Keep iterating until the current pointer exceeds the end pointer

"""
"""
Time: O(n) only traversing the array once
space O(1) since no extra space is used

"""


def sort_colors(colors):
    start, current, end = 0, 0, len(colors) - 1

    while current <= end:
        if colors[current] == 0:
            if colors[start] != 0:
                colors[start], colors[current] = colors[current], colors[start]

            current += 1
            start += 1

        elif colors[current] == 1:
            current += 1

        else:
            if colors[end] != 2:
                colors[current], colors[end] = colors[end], colors[current]

            end -= 1


# Driver code
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        colors = inputs[i]
        print(i + 1, ".\tcolors:", colors)
        sort_colors(colors)
        print("\n\tThe sorted array is:", colors)
        print("-" * 100)


if __name__ == "__main__":
    main()
