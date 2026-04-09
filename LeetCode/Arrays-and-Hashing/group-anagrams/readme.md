# 49. Group Anagrams

[View Problem on LeetCode](https://leetcode.com/problems/group-anagrams/)

**Difficulty:** Medium
**Topic:** Arrays & Hashing

## Approach
The goal is to group an array of strings into sub-lists of anagrams. 

A naive approach would be to sort each string alphabetically. Since anagrams become the exact same string when sorted (e.g., "eat" and "tea" both become "aet"), we could use the sorted string as a hash map key. However, sorting every string takes $O(K \log K)$ time, making the total time complexity $O(N \cdot K \log K)$.

We can optimize this to $O(N \cdot K)$ by using **Character Frequency Arrays**:
1. Two strings are anagrams if and only if their character counts (frequencies) are identical.
2. For each string, we build an array of size 26 to count the occurrences of each lowercase English letter using ASCII math (`ord(c) - ord('a')`).
3. In Python, lists are mutable and cannot be used as dictionary keys. Therefore, we cast the frequency array into an immutable `tuple`.
4. We use this `tuple` as the key in a `defaultdict`. All anagrams will generate the exact same tuple and thus be appended to the same list in the dictionary.

## Complexity Analysis
* **Time Complexity:** $O(N \cdot K)$ where $N$ is the number of strings in the input array and $K$ is the maximum length of a string. We iterate through every character of every string exactly once.
* **Space Complexity:** $O(N \cdot K)$ as we store all the strings grouped in lists within our hash map. The size 26 frequency arrays take $O(1)$ constant space per string.

## Code
The full solution is available in [`solution.py`](./solution.py).