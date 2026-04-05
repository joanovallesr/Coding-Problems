# 1929. Concatenation of Array

[View Problem on LeetCode](https://leetcode.com/problems/concatenation-of-array/)

**Difficulty:** Easy
**Topic:** Arrays & Hashing

## Approach
To concatenate the array to itself, we need to create a new array, `ans`, that is exactly twice the length of the original `nums` array. 

By iterating through the original `nums` array a single time, we can be highly efficient. For every index `i`, we take the value `nums[i]` and simultaneously assign it to the first half of our new array (`ans[i]`) and the exact corresponding spot in the second half (`ans[i + n]`).

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the length of the input array. The loop runs exactly $n$ times. 
* **Space Complexity:** $O(n)$ because we are allocating a brand new array of size $2n$ in memory to store and return the result. 

## Code
The full solution is available in [`solution.py`](./solution.py).