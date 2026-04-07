#include <string>
#include <vector>

using namespace std;

/*
 * 242. Valid Anagram
 * * Approach:
 * If the strings are different lengths, they cannot be anagrams.
 * We use a frequency array of size 26 to count the occurrences of each letter in string 's'.
 * Then, we iterate through string 't', decrementing the counts. 
 * If we ever need to decrement a letter that has a count of 0, 't' has a letter that 's' does not (or has too many of it), so we return false.
 * * Time Complexity: O(n) - Where n is the length of the strings. We iterate through each string once.
 * Space Complexity: O(1) - The frequency vector is always exactly size 26, meaning memory usage does not scale with the input size.
 */
class Solution {
public:
    bool isAnagram(string s, string t) {
        // If lengths differ, they can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }

        // Frequency array for the 26 lowercase English letters
        vector<int> count(26, 0);

        // Build the frequency map for string s
        for (char c : s) {
            count[c - 'a'] += 1;
        }

        // Validate string t against the frequency map
        for (char c : t) {
            if (count[c - 'a'] == 0) {
                return false;
            }
            count[c - 'a'] -= 1;
        }

        return true;
    }
};