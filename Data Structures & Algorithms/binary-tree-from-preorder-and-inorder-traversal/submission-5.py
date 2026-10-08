# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pos = {val: i for i, val in enumerate(inorder)}

        def dfs(pre_start, in_left, in_right):
            
            if in_left > in_right:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            mid = pos[root_val]

            left_size = mid - in_left

            root.left = dfs(
                pre_start + 1,
                in_left,
                mid - 1
            )

            root.right = dfs(
                pre_start + left_size + 1,
                mid + 1,
                in_right
            )

            return root

        return dfs(0, 0, len(inorder) - 1)
        
