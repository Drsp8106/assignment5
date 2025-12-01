# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)


# TEST CASES
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5, 5, 6]) == 5
assert most_frequent([1]) == 1
assert most_frequent([2, 3]) in (2, 3)


"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Counting frequencies is optimal.
- Could it be optimized? No asymptotic improvement possible.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result


# TEST CASES
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([9, 8, 7]) == [9, 8, 7]


"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Set membership is efficient and order is preserved.
- Could it be optimized? No faster order-preserving method exists.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for n in nums:
        complement = target - n
        if complement in seen:
            pairs.append((complement, n))
        seen.add(n)
    return pairs


# TEST CASES
assert sorted(find_pairs([1, 2, 3, 4], 5)) == [(1, 4), (2, 3)]
assert find_pairs([1, 2], 10) == []
assert find_pairs([], 5) == []
assert find_pairs([5, 0, -5], 5) == []


"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Uses set for efficient lookups.
- Could it be optimized? This is the optimal approach.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    arr = [None] * capacity
    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            new_arr = [None] * (capacity * 2)
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
            capacity *= 2
        arr[size] = i
        size += 1
    return arr[:size]


# TEST CASES
add_n_items(6)
add_n_items(1)
add_n_items(0)


"""
Time and Space Analysis for problem 4:
- When do resizes happen? Whenever size == capacity.
- Worst-case for a single append: O(n) due to copying.
- Amortized time per append: O(1).
- Space complexity: O(n).
- Why does doubling reduce cost overall? Because copying happens infrequently.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]

def running_total(nums):
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result


# TEST CASES
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([5]) == [5]
assert running_total([]) == []
assert running_total([10, -10, 5]) == [10, 0, 5]


"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? One pass, minimal overhead.
- Could it be optimized? No — output requires O(n) space.
"""
