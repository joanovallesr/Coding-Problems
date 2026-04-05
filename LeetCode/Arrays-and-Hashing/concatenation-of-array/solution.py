from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Creates an array by concatenating the input array to itself.
        
        Time Complexity: O(n) - We iterate through the input list exactly once.
        Space Complexity: O(n) - We allocate a new list of size 2n for the result.
        """
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans