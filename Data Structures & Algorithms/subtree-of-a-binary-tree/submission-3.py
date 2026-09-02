# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        flag = False

        def same(p, q):

            if not p and not q:
                return True

            if (not p and q) or (p and not q):
                return False
            
            if p.val != q.val:
                return False
            
            left = same(p.left,q.left)
            right = same(p.right, q.right)

            return left and right
        
        def subtree(root, subroot):
            nonlocal flag
            
            if not root:
                return
            
            if same(root,subroot):
                flag = True

            left = subtree(root.left, subroot)
            right = subtree(root.right, subroot)

            return left or right

        subtree(root,subRoot)

        return flag
        

    



    """
    Check if for any given root, if they are the same tree, then second check
    if they a subtree, using the same function
    """