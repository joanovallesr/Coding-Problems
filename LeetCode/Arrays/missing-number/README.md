# 268. Missing Number

### Intuition
The problem asks for a missing number in a range `[0, n]`. If the array were sorted, every number `nums[i]` should ideally be equal to its index `i` (e.g., at index 0 we have 0, at index 1 we have 1). By sorting the array first, we can simply iterate through it and find the first index where this condition fails.

### Approach
1. Sort the input array `nums`.
2. Iterate through the array from `0` to `n-1`.
3. At each index `i`, check if `nums[i]` is equal to `i`.
4. If they are not equal, then `i` is the missing number; return `i`.
5. If the loop completes without finding a mismatch, the missing number must be the largest one, `n`.

### Complexity
* **Time Complexity:** $O(n \log n)$ — dominated by the sorting algorithm.
* **Space Complexity:** $O(\log n)$ — space required for the sorting stack (depending on the specific implementation of `Arrays.sort` for primitives).
