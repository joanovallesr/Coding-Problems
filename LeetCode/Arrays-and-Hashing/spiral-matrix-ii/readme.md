# 59. Spiral Matrix II

[View Problem on LeetCode](https://leetcode.com/problems/spiral-matrix-ii/)

**Difficulty:** Medium
**Topic:** Arrays & Matrix Simulation

## Approach
This is a classic matrix simulation problem. The goal is to fill an empty $n \times n$ matrix with numbers from $1$ to $n^2$ in a clockwise spiral.

Instead of trying to calculate complex mathematical patterns for indices, we use the **Four Boundaries Approach**. We establish four pointers to represent the current unvisited perimeter of the matrix: `top`, `bottom`, `left`, and `right`.

We then simulate the spiral movement using four distinct loops within a `while` loop:
1. **Move Right:** Iterate from `left` to `right` along the `top` row. Once finished, increment `top` to shrink the top boundary downwards.
2. **Move Down:** Iterate from `top` to `bottom` along the `right` column. Once finished, decrement `right` to shrink the right boundary inwards.
3. **Move Left:** Iterate from `right` to `left` along the `bottom` row. Once finished, decrement `bottom` to shrink the bottom boundary upwards.
4. **Move Up:** Iterate from `bottom` to `top` along the `left` column. Once finished, increment `left` to shrink the left boundary inwards.

We repeat this process until the boundaries cross each other (`top > bottom` or `left > right`), meaning the entire matrix has been filled. The inner `if` checks ensure we don't duplicate rows or columns if the matrix is non-square, though for this specific $n \times n$ problem, the boundaries will naturally converge.

## Complexity Analysis
* **Time Complexity:** $O(n^2)$ where $n$ is the given integer. The algorithm must visit and populate every single cell in the $n \times n$ matrix exactly once, resulting in $n^2$ operations.
* **Space Complexity:** $O(n^2)$ to allocate the 2D array that stores the result. If the returned output array is not considered as extra space, the auxiliary space complexity is $O(1)$ since we only use a few integer variables to track the boundaries.

## Code
The full solution is available in [`solution.py`](./solution.py).