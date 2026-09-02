# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(root):
            nonlocal max_diameter 
            
            if not root:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            curr_diameter = left_depth + right_depth
            max_diameter = max(max_diameter, curr_diameter)

            return 1 + max(left_depth, right_depth)
        
        dfs(root)

        return max_diameter







            
            
 