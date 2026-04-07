#include <vector>
#include <unordered_map>

using namespace std;

/*
 * 1. Two Sum
 * * Approach:
 * We use a hash map (unordered_map) to store the numbers we have visited as keys 
 * and their indices as values. For each number 'x', we calculate the 'complement' 
 * (target - x). If the complement is already in the map, we have found our 
 * pair and return their indices.
 * * Time Complexity: O(n) - We traverse the array once. Hash map lookups and 
 * insertions are O(1) on average.
 * Space Complexity: O(n) - In the worst case, we store almost all elements 
 * in the hash map.
 */
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            // If the complement exists in our map, we found the pair
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            
            // Otherwise, store the current number and its index for future lookups
            seen[nums[i]] = i;
        }
        
        return {}; // Should not be reached based on problem constraints
    }
};