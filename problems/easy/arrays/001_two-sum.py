"""
LeetCode Problem: 1 - Two Sum
Difficulty: Easy
Topic: Array
URL: https://leetcode.com/problems/two-sum/

Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Examples:
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        missing_index = {}
        
        for i in range(0, len(nums)):
            
            found = missing_index.get(nums[i], None)
            
            if found is None:
                
                missing = target - nums[i]
                missing_index[missing] = i

            else:
                return [i, found]


# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1: Example 1 from problem
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    
    result1 = sol.twoSum(nums1, target1)
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    print("✅ Test 1 passed: [2,7,11,15], target=9 → [0,1]")
    
    # Test case 2: Example 2 from problem
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    
    result2 = sol.twoSum(nums2, target2)
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    print("✅ Test 2 passed: [3,2,4], target=6 → [1,2]")
    
    # Test case 3: Example 3 from problem (duplicate numbers)
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    
    result3 = sol.twoSum(nums3, target3)
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    print("✅ Test 3 passed: [3,3], target=6 → [0,1]")
    
    print("\n🎉 All test cases passed!")


if __name__ == "__main__":
    test_solution()