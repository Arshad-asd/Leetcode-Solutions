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
# QUESTION NO: 450. Delete Node in a BST

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return 
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            else:
                succ = self.getsucs(root.right,key)
                root.val = succ
                root.right = self.deleteNode(root.right,succ)
        return root
    def getsucs(self,cur,key):
        while cur.left is not None:
            cur = cur.left
        return cur.val

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 701. Insert into a Binary Search Tree
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        if root.val == val:
            return root
        elif root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        return root 

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 938. Range Sum of BST
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def bfs_traverse(node):
            if node is not None:
                nonlocal sums
                if low <= node.val <= high:
                    sums += node.val
                if node.val > low:
                   bfs_traverse(node.left)
                if node.val < high:
                    bfs_traverse(node.right)
        sums = 0
        bfs_traverse(root)
        return sums

'''--------------------------------------------------------------------------------------------'''
