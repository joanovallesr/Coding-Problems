# 1. Two Sum

[View Problem on LeetCode](https://leetcode.com/problems/two-sum/)

**Difficulty:** Easy
**Topic:** Arrays & Hashing

## Approach
The brute-force approach involves a nested loop to check every possible pair, which takes $O(n^2)$ time. To optimize this, we use a **One-Pass Hash Map**.

Instead of looking for the second number after picking the first, we look for the "complement" of the current number as we iterate. For any number `nums[i]`, the complement is `target - nums[i]`. 

1. We initialize an empty hash map (dictionary).
2. For each number in the array:
   - Check if its `complement` exists in the map.
   - If it does, return the index stored in the map and the current index `i`.
   - If it doesn't, add the current number to the map with its index as the value.

This allows us to solve the problem in a single traversal of the array.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the number of elements in the array. We visit each element exactly once, and hash map operations (insertion and lookup) are $O(1)$ on average.
* **Space Complexity:** $O(n)$ because we store up to $n$ elements in the hash map to keep track of indices.

## Code
The full solution is available in [`solution.cpp`](./solution.cpp).