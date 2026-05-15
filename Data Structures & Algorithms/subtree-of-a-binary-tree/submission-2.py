# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(root,subRoot):

            if not root and not subRoot:
                return True
            
            if (root and not subRoot) or (subRoot and not root):
                return False
            
            if root.val != subRoot.val:
                return False
            
            return same(root.left, subRoot.left) and same(root.right, subRoot.right)
        
        def subtree(root):

            if not root:
                return False
            
            if same(root,subRoot):
                return True
        
            return subtree(root.left) or subtree(root.right)
        
        return subtree(root)