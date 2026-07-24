# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursive(node):

            if node is None:
                return 0
            
            else: 
                leftDepth = recursive(node.left)
                rightDepth = recursive(node.right)
                maxDepth = 1 + max(leftDepth, rightDepth)
                return maxDepth
        return recursive(root)

            