# 35. Search Insert Position

### Intuition
Since the input array is **sorted** and the requirement is **$O(\log n)$** time complexity, Binary Search is the optimal approach.

### Approach
1. Initialize `low` at 0 and `hi` at the last index.
2. While `low <= hi`, calculate the `mid` point.
3. If `target` is greater than `nums[mid]`, narrow the search to the right half.
4. If `target` is smaller, narrow it to the left half.
5. If the target isn't found, the `low` index (or `hi + 1`) naturally represents the position where the target would be inserted to maintain order.

### Complexity
* **Time Complexity:** $O(\log n)$ — Each step halves the search space.
* **Space Complexity:** $O(1)$ — Only a few integer variables are used.
