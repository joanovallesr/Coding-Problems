from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        347. Top K Frequent Elements
        
        Time Complexity: O(N) - We iterate through the array to build the frequency map, 
        then iterate through the map to populate the buckets, and finally do a linear 
        scan of the buckets. All operations scale linearly.
        Space Complexity: O(N) - The frequency hash map and the bucket array will 
        store at most N elements.
        """
        # Step 1: Build a frequency map
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        # Step 2: Create an array of empty lists (buckets)
        # The index of the array represents the *frequency* of an element.
        # We need size len(nums) + 1 because the max frequency an element can have is len(nums).
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Populate the buckets. 
        # If the number '3' appears 2 times, we place '3' in buckets[2].
        for n, f in freq.items():
            buckets[f].append(n)

        # Step 4: Gather the top 'k' frequent elements by scanning buckets from right to left
        res = []
        for f in range(len(nums), 0, -1):
            for n in buckets[f]:
                res.append(n)
                if len(res) == k:
                    return res

        return res