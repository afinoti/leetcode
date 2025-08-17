"""
LeetCode Problem: 3 - Longest Substring Without Repeating Characters
Difficulty: Medium
Topic: String, Hash Table, Sliding Window
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Examples:
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""

from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 :
            return 0
        elif len(s) == 1 :
            return 1
        
        
        first = s[0]
        max_sub_len = 1

        latest_letter_positions = { first : 0}
        cur_str = first
        cur_start = 0
        cur_end = 0
        cur_len = 1

        for i in range(1, len(s)):
            l = s[i]

            latest_pos_l = latest_letter_positions.get(l,-1)

            #faz parte substring
            if cur_start <= latest_pos_l <=cur_end:
                new_start = latest_pos_l+1
                new_end = i
                new_sub = s[latest_pos_l+1:i+1]
                new_len = len(new_sub)
            else:
                new_start = cur_start
                new_end = i
                new_sub = cur_str+l
                new_len = cur_len+1


            # print(f"new_sub:{new_sub}")

            if new_len > max_sub_len:

                # print(f"new_len:{new_len}")
                max_sub_len = new_len
                
            cur_len = new_len
            cur_str = new_sub    
            cur_start = new_start
            cur_end = new_end
            latest_letter_positions[l] = i

        return max_sub_len

