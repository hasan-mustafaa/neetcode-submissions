class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: index for index, val in enumerate(inorder)}
        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root = TreeNode(preorder[preorder_index])
            preorder_index += 1

            # Lookup
            mid = inorder_map[root.val]

            # Build the subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)

"""
First node of preorder is the root.
Its position in inorder splits inorder:
    everything before it is the left subtree,
    everything after it is the right subtree.
Build left first, because preorder lists the left subtree before the right.
"""