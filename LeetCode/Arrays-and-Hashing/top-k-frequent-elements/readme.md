# 347. Top K Frequent Elements

[View Problem on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

**Difficulty:** Medium
**Topic:** Arrays & Hashing

## Approach
The goal is to return the $k$ most frequent elements from an array. There are three common ways to solve this:
1. **Sorting (Naive):** Count frequencies with a hash map, then sort the map by values. Time: $O(N \log N)$.
2. **Min-Heap:** Keep a heap of size $k$ that stores the most frequent elements seen so far. Time: $O(N \log K)$.
3. **Bucket Sort (Optimal):** Use an array where the *indices* represent the frequencies. Time: $O(N)$.

This solution implements the **Bucket Sort** approach to achieve linear time complexity:
1. **Frequency Map:** We first iterate through `nums` to count the occurrences of each number using a hash map.
2. **Bucket Array:** We initialize a list of empty lists called `buckets`. We make the size of this array `len(nums) + 1` because the highest possible frequency an element can have is the length of the input array itself (if every element is the same number).
3. **Map to Buckets:** We iterate through our frequency map. For every `(number, frequency)` pair, we append the `number` to the list at `buckets[frequency]`.
4. **Retrieve Top $k$:** Since the indices represent frequencies, the highest frequencies are at the end of the `buckets` array. We iterate backward from the end of the array, appending numbers to our result list until we have collected $k$ elements.

## Complexity Analysis
* **Time Complexity:** $O(N)$ where $N$ is the number of elements in the input array. Building the frequency map takes $O(N)$ time, placing elements into the bucket array takes $O(N)$ time, and scanning the bucket array from right to left takes $O(N)$ time. 
* **Space Complexity:** $O(N)$. The hash map stores up to $N$ distinct elements, and the bucket array allocates lists that collectively hold exactly $N$ elements. 

## Code
The full solution is available in [`solution.py`](./solution.py).