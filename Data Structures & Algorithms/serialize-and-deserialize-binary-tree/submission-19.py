# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        global output
        output = []
        def dfs(node):
            global output
            if not node:
                output.append("N")
                return

            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        global arr
        arr = deque(data.split(","))
        if not arr or arr[0] == "N":
            return None
        head = TreeNode(int(arr.popleft()))

        def dfs(node):
            global arr

            left = arr.popleft()

            if left != "N":
                node.left = TreeNode(int(left))
                dfs(node.left)
            
            right = arr.popleft()
            if right != "N":
                node.right = TreeNode(int(right))
                dfs(node.right)

        dfs(head)

        return head


                



        


