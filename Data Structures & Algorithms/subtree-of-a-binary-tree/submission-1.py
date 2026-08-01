# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isExactTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if not p:
            if not q: return True
            return False
        if not q and p: return False
        
        if p.val != q.val:
            return False

        return self.isExactTree(p.left, q.left) and self.isExactTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if we check is same tree for all subtrees, it is O(V * V * E) = O(V^2 * E)
        # space complexity is still O(1) since in place

        # base case
        if not root: return False
        if not subRoot: return True
        if root.val == subRoot.val:
            if self.isExactTree(root, subRoot):
                return True

        # look for optimizations here
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
