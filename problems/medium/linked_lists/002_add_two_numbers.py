"""
LeetCode Problem: 2 - Add Two Numbers
Difficulty: Medium
Topic: Linked List
URL: https://leetcode.com/problems/add-two-numbers/

Problem Description:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Examples:
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """String representation for debugging"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


class Solution:
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nexts
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        extra_one = 0
        head  = None
        previous_node = None
        
        while  (l1 or l2 or extra_one):


           # print(f"l1:{l1}")
           # print(f"l2:{l2}")
           # print(f"extra_one:{extra_one}")


            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
                l1 = l1.next
            
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
                l2 = l2.next
            

            cur_sum = l1_val + l2_val + extra_one
            cur_dig = cur_sum %10
            extra_one = 1 if cur_sum >= 10 else 0

            cur_node  = ListNode(cur_dig, None)

            if head is None:
                head = cur_node
            else:
                previous_node.next = cur_node
            
            previous_node = cur_node

        return head


    def addTwoNumbersCursor(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Simulate elementary math addition with carry
        Time Complexity: O(max(m, n)) where m and n are lengths of l1 and l2
        Space Complexity: O(max(m, n)) for the result linked list
        
        Algorithm:
        1. Create a dummy head to simplify result construction
        2. Iterate through both lists simultaneously
        3. Add corresponding digits plus any carry from previous addition
        4. Handle carry by using divmod(sum, 10)
        5. Continue until both lists are exhausted and no carry remains
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Continue while there are nodes in either list or carry exists
        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next
    
    