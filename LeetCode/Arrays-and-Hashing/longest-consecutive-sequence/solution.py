from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        128. Longest Consecutive Sequence
        
        Time Complexity: O(n) - Although there is a while loop inside a for loop, 
        the while loop only runs when a number is the start of a sequence. 
        Therefore, each number in the array is visited at most twice (once in 
        the outer loop, and at most once in the inner loop).
        Space Complexity: O(n) - We store all elements of the input array inside 
        a Hash Set for O(1) average time complexity lookups.
        """
        s = set(nums)
        best = 0

        for num in s:
            # Check if this number is the start of a sequence
            if num - 1 not in s:          
                length = 1
                nxt = num + 1
                
                # Count the length of the consecutive sequence
                while nxt in s:
                    length += 1
                    nxt += 1
                    
                # Update the maximum sequence length found so far
                best = max(best, length)
                
        return best