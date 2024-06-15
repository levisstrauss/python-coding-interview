"""
Given a string, s, that represents a DNA subsequence, and a number k
, return all the contiguous subsequences (substrings) of length 𝑘
that occur more than once in the string. The order of the returned
subsequences does not matter. If no repeated substring is found, the
function should return an empty set.
"""

"""
Repeat

Time O((n - k) x k)

Space O(1 + n + n - k + 1) = O(n)


"""

def find_repeated_sequences(s, k):
    if len(s) < k:
        return set()

    # Mapping for nucleotides to integers
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    a = 4  # Base for rolling hash
    n = len(s)

    # Convert sequence to numbers based on mapping
    numbers = [mapping[char] for char in s]

    # Initial hash value for the first window
    hash_value = sum(numbers[i] * (a ** (k - i - 1)) for i in range(k))
    hash_set = {hash_value}
    output = set()

    # Precompute a^(k-1) for rolling hash updates
    a_k_minus_1 = a ** (k - 1)

    for i in range(1, n - k + 1):
        # Rolling hash: remove leftmost and add rightmost value
        hash_value = (hash_value - numbers[i - 1] * a_k_minus_1) * a + numbers[i + k - 1]

        # If hash is already seen, add the sequence to the output
        if hash_value in hash_set:
            output.add(s[i:i + k])
        else:
            hash_set.add(hash_value)

    return output