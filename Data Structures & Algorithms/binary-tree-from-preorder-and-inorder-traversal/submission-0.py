# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        # 1. Preorder's first value is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        # 2. Find the root in inorder
        mid = inorder.index(root_val)
        # 3. Everything left of mid belongs to the left subtree
        root.left = self.buildTree(
            preorder[1 : mid + 1],
            inorder[:mid]
        )
        # 4. Everything right of mid belongs to the right subtree
        root.right = self.buildTree(
            preorder[mid + 1 :],
            inorder[mid + 1 :]
        )

        return root
        




