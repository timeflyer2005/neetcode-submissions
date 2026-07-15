class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Longest path passing through this node
            self.diameter = max(
                self.diameter,
                left_height + right_height
            )

            # Return this subtree's height to the parent
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter