'''
给定一个二叉树，返回它的中序 遍历。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 1.递归法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        if root != None:
            res = []
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
            return res
        else:
            return []
# 2.迭代法-用栈
    def inorder_Iteration(self,root:TreeNode):
        stack = []
        res = []
        while root or stack:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                cur_node = stack.pop()
                res.append(cur_node.val)
                root = cur_node.right
        return res

'''
给定一个二叉树，返回它的 前序遍历。
'''
class Solution:
# 1.递归
    def preorderTraversal(self, root: TreeNode) -> [int]:
        if root != None:
            res = []
            res.append(root.val)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
            return res
        else:
            return []
# 2.迭代
    def preorder_iteration(self,root:TreeNode):
        stack = []
        res = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                cur_node = stack.pop()
                root = cur_node.right
        return res












