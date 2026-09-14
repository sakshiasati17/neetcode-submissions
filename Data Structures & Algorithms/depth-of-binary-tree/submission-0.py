# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs (node,h):
            
            if not node:
                return 0
            h+=1
            if not node.left and not node.right:
                return h
            left_result = dfs(node.left, h)
            right_result = dfs(node.right, h)
            return max(left_result, right_result)
        return dfs(root,0)
            
        