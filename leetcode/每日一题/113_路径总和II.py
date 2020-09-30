# -*- coding:utf-8 -*-
# @Time: 2020/9/26 9:28
# @Author: Lj
# @File: 113_路径总和II.py

'''
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> [[]]:
        res = []
        def dfs(root,sum,path):
            if not root.left and not root.right:
                if root.val == sum:
                    path += [root.val]
                    res.append(path)
                return
            if root.left:
                dfs(root.left, sum-root.val, path+[root.val])
            if root.right:
                dfs(root.right, sum-root.val, path+[root.val])

        if not root:
            return res
        dfs(root, sum_, [])
        return res

#测试
from leetcode.BinaryTree.NodeAndBuildTree import *

lst = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
root = list_buildTree(lst)
BFS(root)

res = Solution().pathSum(root, 22)
print(res)