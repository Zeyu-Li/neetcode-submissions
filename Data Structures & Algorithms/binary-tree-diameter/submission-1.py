# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    dp = {None: 0}
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if dfs, time complexity is O(n), worst case we visit all the nodes
        # space complexity O(1), we don't need to allocate extra space
        # bfs probably best way

        # base case
        if not root: return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # notice that is the length of the longest 2 subtrees added together
        # this is bfs so we are exploring all O(E+V) time complexity
        # in place recursion so O(1) space

        # base case
        if not root: return 0

        if root.left in self.dp:
            l_max = self.dp[root.left]
        else:
            l_max = self.maxDepth(root.left)
            self.dp[root.left] = l_max

        if root.right in self.dp:
            r_max = self.dp[root.right]
        else:
            r_max = self.maxDepth(root.right)
            self.dp[root.right] = r_max


        root_len = l_max + r_max
        l_len = self.diameterOfBinaryTree(root.left)
        r_len = self.diameterOfBinaryTree(root.right)

        return max(root_len, l_len, r_len)