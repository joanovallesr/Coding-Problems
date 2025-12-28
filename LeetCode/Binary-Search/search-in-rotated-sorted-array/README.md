# 33. Search in Rotated Sorted Array

### Intuition
In a standard sorted array, we can determine exactly which half to ignore based on the `mid` value. In a **rotated** sorted array, one half of the array (split by `mid`) will always remain sorted, while the other half contains the rotation. By identifying which half is sorted, we can check if the `target` lies within that sorted range. If it does, we search there; otherwise, we search the other half.

### Approach
1. Initialize `lo` and `hi`.
2. Calculate `mid`. Check if `nums[mid]` is the target.
3. Determine which side is sorted:
   * **Left Sorted (`nums[lo] <= nums[mid]`):** If the target lies between `nums[lo]` and `nums[mid]`, move `hi` to `mid - 1`. Otherwise, move `lo` to `mid + 1`.
   * **Right Sorted (`nums[mid] <= nums[hi]`):** If the target lies between `nums[mid]` and `nums[hi]`, move `lo` to `mid + 1`. Otherwise, move `hi` to `mid - 1`.
4. Repeat until found or `lo > hi`.

### Complexity
* **Time Complexity:** $O(\log n)$ — We still halve the search space in every iteration.
* **Space Complexity:** $O(1)$ — No extra space is required.
