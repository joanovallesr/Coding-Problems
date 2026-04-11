from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        238. Product of Array Except Self
        
        Time Complexity: O(N) - We make two separate passes through the array 
        (one forward, one backward). Both take linear time.
        Space Complexity: O(1) auxiliary space - The problem states the output array 
        does not count toward space complexity. We only use two integer variables 
        ('prefix' and 'suffix') for our calculations.
        """
        n = len(nums)
        # Initialize the output array with 1s
        answer = [1] * n

        # First pass: Calculate the product of all elements to the left of index 'i'
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Second pass: Calculate the product of all elements to the right of index 'i'
        # and multiply it with the existing prefix product in the answer array
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer