#include <vector>
#include <string>
#include <algorithm>

using namespace std;

/*
 * 14. Longest Common Prefix
 * * Approach:
 * We leverage lexicographical sorting. By sorting the array of strings, the 
 * strings that are most different from each other will end up at the first 
 * and last positions. We then only need to compare these two strings character 
 * by character to find the longest common prefix for the entire array.
 * * Time Complexity: O(N * M * log N) - Where N is the number of strings and 
 * M is the maximum length of a string. Sorting takes O(N log N) comparisons, 
 * and each string comparison can take up to O(M) time.
 * Space Complexity: O(1) or O(log N) - Depending on the language's sorting 
 * algorithm implementation (C++ std::sort typically uses O(log N) auxiliary stack space).
 */
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";

        // Sort the array lexicographically
        sort(strs.begin(), strs.end());
        
        int n = strs.size();
        string first = strs[0];
        string last = strs[n - 1];

        // Compare the first and last strings up to the length of the shorter one
        for (int i = 0; i < min(first.size(), last.size()); i++) {
            if (first[i] != last[i]) {
                return ans;
            }
            ans += first[i];
        }

        return ans;
    }
};