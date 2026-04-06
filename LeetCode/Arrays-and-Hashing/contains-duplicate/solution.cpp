#include <vector>
#include <unordered_set>

using namespace std;

/*
 * 217. Contains Duplicate
 * * Approach:
 * We use a Hash Set to track the numbers we have seen so far. As we iterate
 * through the array, we check if the current number is already in the set.
 * If it is, we found a duplicate and return true. If not, we insert it.
 * * Time Complexity: O(n) - We traverse the array at most once. Hash set 
 * insertions and lookups take O(1) time on average.
 * Space Complexity: O(n) - In the worst case (no duplicates), the hash set 
 * will grow to the same size as the input array.
 */
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for (int n : nums) {
            // If the number is already in the set, we found a duplicate
            if (seen.count(n)) {
                return true;
            }
            
            // Otherwise, add it to the set and keep going
            seen.insert(n);
        }

        // If the loop finishes without returning true, all elements are unique
        return false;
    }
};