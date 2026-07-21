# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while True:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left
            # Visit the next-smallest node
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            # Then explore its right subtree
            current = current.right