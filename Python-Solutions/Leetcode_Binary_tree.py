                                                     # BINARY TREE LEETCODE SOLUTIONS
'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 257. Binary Tree Paths

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def travers(root,path):
            if not root:
                return []
            if not(root.left or root.right):
                return result.append(path+str(root.val))
            if root.left:
                travers(root.left,path+str(root.val)+"->")
            if root.right:
                travers(root.right,path+str(root.val)+"->")
        travers(root,"")
        return result

'''--------------------------------------------------------------------------------------------'''
