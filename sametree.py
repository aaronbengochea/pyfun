
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DataTreeNode(TreeNode):

    def __init__(self, val=0, left=None, right=None, adData=None):
        super().__init__(val,left,right)
        self.adData = adData

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
    
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # There will always be a root and a subroot

        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.sameSubtree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot.right) and self.isSubtree(root.right, subRoot.right)

    
    def sameSubtree(self, root: TreeNode, subRoot: TreeNode):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.sameSubtree(root.right, subRoot.right) and self.sameSubtree(root.left, subRoot.left)

        return False



def main():

    #Creating different Trees
    x = TreeNode(1)
    y = TreeNode(2)
    z = TreeNode(3)
    a = DataTreeNode(5, adData=555)
    x.left = a
    x.right = y
    y.right = z

    x1 = TreeNode(1)
    y1 = TreeNode(2)
    a1 = DataTreeNode(5, adData=555)
    x1.left = a1
    x1.right = y1


    x2 = TreeNode(1)
    y2 = TreeNode(2)
    a2 = DataTreeNode(5, adData=555)
    x2.left = a2

    x3 = TreeNode(1)
    y3 = TreeNode(2)
    a3 = DataTreeNode(5, adData=555)
    x3.left = a3
    
    # Creating sameTree solutions
    solution = Solution()
    result1 = solution.isSameTree(x, x1)
    result2 = solution.isSameTree(x, x2)
    result3 = solution.isSameTree(x2, x3)
    print("x & x1 (False): ", result1)
    print("x & x2 (False): ", result2)
    print("x2 & x3 (True): ", result3)

    # Creating maxDepth solutions
    result4 = solution.maxDepth(x)
    result5 = solution.maxDepth(x1)
    print("max Depth (x): ", result4)
    print("max Depth (x1): ", result5)

    # Creating isSubtree solutions
    result6 = solution.isSubtree(x,y)
    print("isSubTree: ", result6)


        
if __name__ == "__main__":
    main()
