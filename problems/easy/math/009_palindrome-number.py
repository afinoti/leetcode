"""
LeetCode Problem: 9 - Palindrome Number
Difficulty: Easy
Topic: Math
URL: https://leetcode.com/problems/palindrome-number/

Problem Description:
Given an integer x, return true if x is a palindrome, and false otherwise.

Examples:
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

from typing import List, Optional


class Solution:

    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        middle = int(len(s)/2)
        for i in range(0, middle):
            if s[i] != s[len(s)-i-1]:
                return False

        return True

    def isPalindromeCursor(self, x: int) -> bool:
        """
        Approach 1: String conversion method
        Time Complexity: O(log n) where n is the input number
        Space Complexity: O(log n) for string conversion
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert to string and compare with its reverse
        str_x = str(x)
        return str_x == str_x[::-1]
    

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1: Positive palindrome
    assert sol.isPalindrome(121) == True
    assert sol.isPalindromeOptimal(121) == True
    print("✅ Test 1 passed: 121 is palindrome")
    
    # Test case 2: Negative number
    assert sol.isPalindrome(-121) == False
    assert sol.isPalindromeOptimal(-121) == False
    print("✅ Test 2 passed: -121 is not palindrome")
    
    # Test case 3: Number ending with 0
    assert sol.isPalindrome(10) == False
    assert sol.isPalindromeOptimal(10) == False
    print("✅ Test 3 passed: 10 is not palindrome")
    
    # Test case 4: Single digit
    assert sol.isPalindrome(7) == True
    assert sol.isPalindromeOptimal(7) == True
    print("✅ Test 4 passed: 7 is palindrome")
    
    # Test case 5: Zero
    assert sol.isPalindrome(0) == True
    assert sol.isPalindromeOptimal(0) == True
    print("✅ Test 5 passed: 0 is palindrome")
    
    # Test case 6: Even digits palindrome
    assert sol.isPalindrome(1221) == True
    assert sol.isPalindromeOptimal(1221) == True
    print("✅ Test 6 passed: 1221 is palindrome")
    
    # Test case 7: Not a palindrome
    assert sol.isPalindrome(123) == False
    assert sol.isPalindromeOptimal(123) == False
    print("✅ Test 7 passed: 123 is not palindrome")
    
    print("\n🎉 All test cases passed!")


if __name__ == "__main__":
    test_solution()
