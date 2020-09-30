# -*- coding:utf-8 -*-
# @Time: 2020/9/29 11:00
# @Author: Lj
# @File: 145_二叉树的后续遍历.py

'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
不用递归用迭代的思路：
    借鉴图的dfs的迭代版
        用stack存储父节点
'''
class Solution:
    #递归版
    def postorderTraversal_1(self,root) -> [int]:
        path = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            path.append(root.val)

        helper(root)
        return path

    #迭代版1
    def postorderTraversal_2(self,root) -> [int]:
        stack = [root]
        visited = set()
        path = []

        while stack:
            parent = stack[-1]
            left = parent.left
            if left and left not in visited:
                stack.append(left)
                visited.add(left)
                continue
            right = parent.right
            if right and right not in visited:
                stack.append(right)
                visited.add(right)
                continue
            cur = stack.pop()
            path.append(cur.val)
        return path

    #迭代版2
    def postorderTraversal_3(self,root) -> [int]:
        stack = []
        path = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left if cur.left else cur.right
            cur = stack.pop()
            path.append(cur.val)
            if stack and stack[-1].left == cur:
                cur = stack[-1].right
            else:
                cur = None
        return path

#测试
from leetcode.BinaryTree.NodeAndBuildTree import *
lst = [1,None,2,None,None,3]
root = list_buildTree(lst)

path = Solution().postorderTraversal_3(root)
print(path)