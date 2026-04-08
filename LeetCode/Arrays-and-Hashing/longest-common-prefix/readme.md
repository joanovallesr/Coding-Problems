# 14. Longest Common Prefix

[View Problem on LeetCode](https://leetcode.com/problems/longest-common-prefix/)

**Difficulty:** Easy
**Topic:** Arrays & Strings

## Approach
A common way to solve this is "Vertical Scanning," where you look at the first character of all strings, then the second character of all strings, and so on. While effective, it requires nested loops and careful boundary checks.

This solution uses a highly elegant alternative: **Lexicographical Sorting**.

1. **Sort the Array:** When an array of strings is sorted alphabetically, the strings that share the most starting characters will be grouped together. Conversely, the strings with the most different prefixes will end up at the very beginning and the very end of the array.
2. **Compare First and Last:** Because the first and last strings in the sorted array are the most different, the common prefix of the *entire* array is simply the common prefix of *just* these two strings.
3. We iterate through the first and last strings simultaneously. As soon as we find a character mismatch, we stop and return the accumulated prefix.

## Complexity Analysis
* **Time Complexity:** $O(N \cdot M \log N)$ where $N$ is the number of strings in the array and $M$ is the maximum length of a string. Sorting the array takes $O(N \log N)$ comparisons, and comparing strings takes $O(M)$ time per comparison. The final linear scan between the first and last string takes $O(M)$ time. *(Note: Vertical scanning is $O(N \cdot M)$, making this sorting approach slightly slower mathematically, but often faster in practice on smaller datasets due to highly optimized standard library sorting).*
* **Space Complexity:** $O(1)$ auxiliary space, excluding the space required to return the output string and the underlying memory stack used by the `std::sort` algorithm (which is typically $O(\log N)$ in C++).

## Code
The full solution is available in [`solution.cpp`](./solution.cpp).