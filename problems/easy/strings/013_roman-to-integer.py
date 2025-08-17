"""
LeetCode Problem: 13 - Roman to Integer
Difficulty: Easy
Topic: String
URL: https://leetcode.com/problems/roman-to-integer/

Problem Description:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Examples:
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXC"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        
        l_values = {
            "I" :   1,
            "V" :   5,
            "X" :   10,
            "L" :   50,
            "C" :   100,
            "D" :   500,
            "M" :   1000,
            "-" :   10000
        }

        last_l = "-"
        total = 0
        cur_sub_value = 0

        for l in s:
            cur_l_v = l_values[l]

            if l_values[ last_l ] > cur_l_v :
                total +=  cur_sub_value
                cur_sub_value = cur_l_v

            elif l_values[ last_l ] == cur_l_v :
                cur_sub_value +=cur_l_v

            else:
                cur_sub_value =  cur_l_v - cur_sub_value

            last_l = l

        total += cur_sub_value          

        return total


# Alternative solution using subtraction pairs
class SolutionAlternative:
    def romanToInt(self, s: str) -> int:
        """
        Alternative approach using subtraction pairs mapping.
        """
        # Map subtraction cases first, then individual characters
        roman_map = {
            'IV': 4, 'IX': 9,
            'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900,
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        i = 0
        
        while i < len(s):
            # Check for two-character subtraction cases first
            if i + 1 < len(s) and s[i:i+2] in roman_map:
                result += roman_map[s[i:i+2]]
                i += 2
            else:
                result += roman_map[s[i]]
                i += 1
        
        return result

