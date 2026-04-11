# 271. Encode and Decode Strings

[View Problem on LeetCode](https://leetcode.com/problems/encode-and-decode-strings/) *(Premium)*

**Difficulty:** Medium
**Topic:** Arrays & Hashing

## Approach
The goal is to design an algorithm to encode a list of strings into a single string, and then decode that single string back into the original list of strings. 

**The Delimiter Collision Problem:**
A naive approach would be to join the strings using a unique character, like a comma or a pipe (`"word1|word2"`). However, this fails if the original strings contain that character (e.g., `["hello|world", "test"]`). The decoder wouldn't know if the `|` is a separator or part of the word.

**The Solution: Length-Prefixing (Chunked Encoding)**
To guarantee we never accidentally split a string, we prefix every string with its exact integer length, followed by a designated delimiter (like `#`). 

1. **Encode:** A list like `["we", "say", ":", "yes"]` becomes `"2#we3#say1#:3#yes"`.
2. **Decode:** We use a pointer `i` to read the string. We find the next `#`. The number before the `#` tells us exactly how many characters to read next. Because we are strictly reading a set number of characters based on the prefix, it doesn't matter if the word itself is full of `#` symbols or numbers; the decoder will consume them safely as part of the string.

## Complexity Analysis
* **Time Complexity:** $O(N)$ for both encoding and decoding, where $N$ is the total number of characters across all strings. Both functions require a single pass through the data.
* **Space Complexity:** $O(N)$ for both encoding and decoding. The encoded string takes $O(N)$ space, and the decoded array takes $O(N)$ space.

## Code
The full solution is available in [`solution.py`](./solution.py).