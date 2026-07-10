# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr1 = list1
        curr2 = list2
        while curr1:
            arr.append(curr1.val)
            curr1 = curr1.next
        
        while curr2:
            arr.append(curr2.val)
            curr2 = curr2.next
        
        arr.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next