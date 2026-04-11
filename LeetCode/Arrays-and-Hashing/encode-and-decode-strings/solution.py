from typing import List

class Solution:
    """
    271. Encode and Decode Strings
    
    Approach: Length-Prefixing
    To prevent delimiter collision (e.g., when a string contains the delimiter itself), 
    we prefix every string with its length and a special character (like '#'). 
    Format: <length>#<string>
    Example: ["lint", "code"] -> "4#lint4#code"
    
    Time Complexity:
    - Encode: O(N) where N is the total number of characters across all strings.
    - Decode: O(N) where N is the length of the encoded string. We traverse it exactly once.
    
    Space Complexity:
    - Encode: O(N) to store the combined encoded string.
    - Decode: O(N) to store the resulting decoded array of strings.
    """

    def encode(self, strs: List[str]) -> str:
        # Join each string formatted as "length#string"
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i, n = [], 0, len(s)

        while i < n:
            # Find the next delimiter '#' starting from our current index 'i'
            j = s.find('#', i)
            
            # The length of the upcoming string is between 'i' and 'j'
            length = int(s[i:j])
            
            # The actual string starts immediately after the '#'
            start = j + 1
            
            # Slice the exact string length and append to results
            res.append(s[start: start + length])
            
            # Move the pointer 'i' to the start of the next encoded block
            i = start + length
        
        return res