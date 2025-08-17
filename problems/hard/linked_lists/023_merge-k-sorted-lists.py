"""
LeetCode Problem: 23 - Merge k Sorted Lists
Difficulty: Hard
Topic: LinkedList
URL: https://leetcode.com/problems/merge-k-sorted-lists/

Problem Description:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Examples:
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""

from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        MAX_VALUE = int(10e4)

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        smallest = MAX_VALUE +1
        for l in lists:


            if  l is not None \
                and l.val < smallest:
                smallest  = l.val        
        
        first = ListNode(None)
        last  = first
        
        j = smallest
        while j <= MAX_VALUE:

            smallest = MAX_VALUE +1

            for i in range(0, len(lists)):
                while  lists[i] is not None:
                    if lists[i].val == j:
                        new_n = ListNode(lists[i].val)
                        last.next = new_n
                        lists[i]  = lists[i].next
                        last = new_n
                    else:
                        if lists[i].val < smallest:
                            smallest = lists[i].val
                        break

            j = smallest

        return first.next
    
    def mergeKListsCursor(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 1: Min-Heap (Priority Queue)
        - Use a min-heap to always get the smallest node among all list heads
        - Push the head of each non-empty list into the heap
        - Extract the minimum, add to result, and push the next node from that list
        
        Time Complexity: O(n log k) where n is total nodes and k is number of lists
        Space Complexity: O(k) for the heap
        """
        if not lists:
            return None
        
        # Min-heap to store (node_value, list_index, node)
        heap = []
        
        # Initialize heap with head nodes of all non-empty lists
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        # Dummy node to simplify list construction
        dummy = ListNode(0)
        current = dummy
        
        # Process all nodes
        while heap:
            val, list_idx, node = heapq.heappop(heap)
            
            # Add current minimum to result
            current.next = ListNode(val)
            current = current.next
            
            # If the list has more nodes, push the next node
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        return dummy.next
    
    