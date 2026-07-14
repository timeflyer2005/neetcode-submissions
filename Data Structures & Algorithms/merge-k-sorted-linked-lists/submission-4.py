# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        dummy = ListNode()
        tail = dummy

        while min_heap:
            value, list_index, node = heapq.heappop(min_heap)
                
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_index, node.next))

        return dummy.next
            