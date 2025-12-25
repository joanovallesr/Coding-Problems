class Solution {
    public int searchInsert(int[] nums, int target) {
        // lowest and highest numbers in range
        int low = 0;
        int hi = nums.length - 1;

        // implement binary search
        while (low <= hi) {
            int mid = low + (hi - low) / 2;
            if (target > nums[mid]) {
                low = mid + 1;
            } else if (target < nums[mid]) {
                hi = mid - 1;
            } else {
                return mid;
            }
        }
        // if target is not in nums, return hi + 1
        return hi + 1;
    }
}
