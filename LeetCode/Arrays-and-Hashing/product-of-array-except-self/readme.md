# 238. Product of Array Except Self

[View Problem on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

**Difficulty:** Medium
**Topic:** Arrays & Hashing

## Approach
The goal is to return an array where every element at index `i` is the product of all the numbers in the original array *except* `nums[i]`. 

**The Constraint:** We are strictly forbidden from using the division operator. If we could use division, we would simply multiply all elements together and divide by `nums[i]` for each position.

**The Solution:**
Instead of division, we can find the product of all elements to the **left** of `i`, and the product of all elements to the **right** of `i`. Multiplying these two values together gives us the product of everything except `i`.

To optimize space, we avoid creating separate `left_products` and `right_products` arrays:
1. **Prefix Pass (Left to Right):** We initialize our `answer` array with `1`s. We iterate forward through the input array, keeping a running `prefix` product. We assign the current `prefix` to `answer[i]`, and then update `prefix` by multiplying it by `nums[i]`.
2. **Suffix Pass (Right to Left):** We iterate backward through the input array, keeping a running `suffix` product. We multiply the existing value in `answer[i]` (which currently holds the left-side product) by the current `suffix`. We then update `suffix` by multiplying it by `nums[i]`.

## Complexity Analysis
* **Time Complexity:** $O(N)$ where $N$ is the number of elements in the array. We make exactly two passes through the array, scaling linearly with the input size.
* **Space Complexity:** $O(1)$ auxiliary space. The problem specifically states that the output array does not count toward space complexity. Because we compute the products directly inside the output array and only use a few tracking variables (`prefix`, `suffix`), our extra space usage is constant.

## Code
The full solution is available in [`solution.py`](./solution.py).