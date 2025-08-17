"""
LeetCode Problem: 4 - Median of Two Sorted Arrays
Difficulty: Hard
Topic: Array
URL: https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median 
of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Examples:
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        result = []
        
        len_num1 = len(nums1)
        len_num2 = len(nums2)

        totalLen = len_num1 + len_num2
        
        i_nums1 = 0
        i_nums2 = 0
        oo

        for i in range(totalLen):

            next_eval = 0
            if i_nums1 >= len_num1:
                result.append(nums2[i_nums2])
                i_nums2 += 1
            elif i_nums2 >= len_num2:
                result.append(nums1[i_nums1])
                i_nums1 += 1
            elif nums1[i_nums1] <= nums2[i_nums2] :
                result.append(nums1[i_nums1])
                i_nums1 += 1
            else:
                result.append(nums2[i_nums2])
                i_nums2 += 1

        middle = totalLen/2

        if totalLen %2 == 0:
            middle1 = int(totalLen/2)
            middle2 = int(totalLen/2) - 1
            return (result[middle1] + result[middle2])/2
        else:
            return result[int((totalLen-1)/2)]
        
    def findMedianSortedArraysOptimizedMerge(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Optimized Merge (only track median positions)
        - Don't create full merged array, just track elements at median positions
        
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        m, n = len(nums1), len(nums2)
        total = m + n
        
        # We need to find element(s) at position(s) for median
        if total % 2 == 0:
            # Even length: need elements at positions (total//2 - 1) and (total//2)
            pos1, pos2 = total // 2 - 1, total // 2
            need_two = True
        else:
            # Odd length: need element at position (total//2)
            pos1 = pos2 = total // 2
            need_two = False
        
        i = j = current_pos = 0
        val1 = val2 = 0
        
        while current_pos <= pos2:
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                current_val = nums1[i]
                i += 1
            else:
                current_val = nums2[j]
                j += 1
            
            if current_pos == pos1:
                val1 = current_val
            if current_pos == pos2:
                val2 = current_val
                break
            
            current_pos += 1
        
        return (val1 + val2) / 2 if need_two else val2
