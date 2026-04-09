from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        49. Group Anagrams
        
        Time Complexity: O(N * K) - Where N is the number of strings and K is the 
        maximum length of a string. We iterate through each string, and for each 
        string, we iterate through its characters.
        Space Complexity: O(N * K) - In the worst case, all strings are unique 
        (no anagrams), and we store every string in our hash map.
        """
        # defaultdict(list) automatically creates an empty list for any new key
        ans = defaultdict(list)

        for s in strs:
            # Create a frequency array of size 26 for the lowercase alphabet
            count = [0] * 26
            
            # Map each character to its corresponding index (0-25)
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            # Convert the list to an immutable tuple so it can be used as a dictionary key
            ans[tuple(count)].append(s)

        # Return just the grouped lists, discarding the tuple keys
        return list(ans.values())