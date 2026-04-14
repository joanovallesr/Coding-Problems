# 128. Longest Consecutive Sequence

[View Problem on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)

**Difficulty:** Medium
**Topic:** Arrays & Hashing

## Approach
The goal is to find the length of the longest consecutive elements sequence in an unsorted array. The problem explicitly demands an algorithm that runs in $O(n)$ time.

**The $O(n \log n)$ Trap:**
The most obvious solution is to sort the array and then iterate through it to count consecutive numbers. However, standard sorting algorithms are bounded by $O(n \log n)$ time complexity, which violates the strict $O(n)$ constraint of this problem.

**The $O(n)$ Set Optimization:**
To achieve linear time, we can trade space for time by using a Hash Set. 
1. Convert the input array into a Hash Set. This allows us to look up the existence of any number in $O(1)$ average time.
2. Iterate through the set. For every number, we ask one crucial question: *Is this the start of a sequence?*
3. We know a number is the start of a sequence if its left neighbor (`num - 1`) does **not** exist in the set.
4. If it is the start, we begin a `while` loop, checking for `num + 1`, `num + 2`, etc., incrementing our current sequence length until the chain breaks.
5. If it is *not* the start (meaning `num - 1` is in the set), we simply skip it. We will eventually count it when we find the true start of its sequence.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the number of elements in the array. Converting the array to a set takes $O(n)$ time. Because we strictly enforce the rule that the inner `while` loop only triggers at the *start* of a sequence, the inner loop will only ever process each number in the array a maximum of one time. Thus, the total iterations across both loops are strictly bounded by $2n$, resulting in an $O(n)$ linear runtime.
* **Space Complexity:** $O(n)$ because we allocate a Hash Set that stores up to $n$ unique elements from the input array.

## Code
The full solution is available in [`solution.py`](./solution.py).