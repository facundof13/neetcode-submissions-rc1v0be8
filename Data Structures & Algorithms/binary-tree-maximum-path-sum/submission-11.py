# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global answer 
        answer = root.val

        def dfs(node):
            if not node:
                return 0

            left_val = dfs(node.left)
            right_val = dfs(node.right)

            global answer
            answer = max(answer, left_val + right_val + node.val)

            return max(left_val + node.val, right_val + node.val, 0)

        
        dfs(root)
        return answer
            