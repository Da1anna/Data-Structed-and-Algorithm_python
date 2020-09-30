# -*- coding:utf-8 -*-
# @Time: 2020/9/28 21:12
# @Author: Lj
# @File: 117_填充每个节点的下一个右侧节点指针.py

class Node:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self,root) -> Node:
        queue = [root]
        while queue:
            i = 0
            k = len(queue)
            while i < k-1:
                queue[i].next = queue[i+1]
                i += 1

            for _ in range(k):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

#测试
from leetcode.BinaryTree.NodeAndBuildTree import *

lst = [1,2,3,4,5,None,7]
root = list_buildTree(lst)

res = Solution().connect(root)
print(root.left.right.next.next)