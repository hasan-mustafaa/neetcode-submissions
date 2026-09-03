# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            
            inorder_map = {val:index for index, val in enumerate(inorder)}
            preorder_index = 0

            def build(left, right):
                nonlocal preorder_index
    
                if left > right:
                    return None

                
                root = TreeNode(preorder[preorder_index])
                preorder_index += 1

                #Lookup
                mid = inorder_map[root.val]


                #Iterate through the tree
                root.left = build(left, mid - 1)
                root.right = build(mid + 1, right)

                return root
        
            return build(0, len(inorder) - 1)






"""
First Node of Preorder is Root
Iterate through Inorder till you find root, (thats left subtree)
Iterate everything after root thats right subtree
"""