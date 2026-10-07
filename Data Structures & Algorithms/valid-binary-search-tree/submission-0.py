# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,left_range,right_range):
            if not node:
                return True
            if node.val >left_range and node.val < right_range:
                return dfs(node.left,left_range,node.val) and dfs(node.right,node.val,right_range)
            else:
                return False
        return dfs(root,float("-inf"),float("inf"))
