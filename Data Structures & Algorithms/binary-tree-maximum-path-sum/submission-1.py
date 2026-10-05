# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=root.val
        def pathSum(root):
            nonlocal res
            if not root:
                return 0
            left = max(0,pathSum(root.left))
            right = max(0,pathSum(root.right))
            res = max(res,root.val+left+right)
            return root.val+max(left,right)
        pathSum(root)
        return res
        

