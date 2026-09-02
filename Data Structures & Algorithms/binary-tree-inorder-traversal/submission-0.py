# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        self.result = []       # creates an attribute called "result" ON the Solution object
        self.dfs(root)
        return self.result
    
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.result.append(node.val)   # accessing that SAME attribute from a different method
        self.dfs(node.right)

        