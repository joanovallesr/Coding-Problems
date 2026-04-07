# 242. Valid Anagram

[View Problem on LeetCode](https://leetcode.com/problems/valid-anagram/)

**Difficulty:** Easy
**Topic:** Arrays & Hashing

## Approach
An anagram is a word formed by rearranging the letters of a different word, meaning both strings must have the exact same character frequencies and the exact same length.

1. **Early Exit:** We first check if the lengths of `s` and `t` are different. If they are, we can immediately return `false`.
2. **Frequency Mapping:** Instead of a Hash Map, we use a fixed-size array of 26 integers to represent the lowercase English alphabet. We iterate through string `s`, incrementing the count for each character using ASCII math (`c - 'a'` maps 'a' to index 0, 'b' to 1, etc.).
3. **Validation:** We then iterate through string `t`. For each character, we check our frequency array. If the count is `0`, it means `t` contains a character (or too many of a character) that doesn't exist in `s`, so we return `false`. Otherwise, we decrement the count.

If we successfully iterate through `t` without hitting a `0`, we have a valid anagram.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the length of the strings. We iterate through string `s` once and string `t` once, resulting in linear time execution.
* **Space Complexity:** $O(1)$ constant space. Regardless of how long the input strings are, our frequency array will always allocate exactly 26 integer spaces.

## Code
The full solution is available in [`solution.cpp`](./solution.cpp).