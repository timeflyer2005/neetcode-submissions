
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hashMap = {None: None}

        curr = head

        # Create every copied node
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        # Connect the copied nodes
        while curr:
            copy = hashMap[curr]

            copy.next = hashMap[curr.next]
            copy.random = hashMap[curr.random]

            curr = curr.next

        return hashMap[head]

