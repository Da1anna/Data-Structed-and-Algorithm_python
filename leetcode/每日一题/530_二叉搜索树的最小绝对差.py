# -*- coding:utf-8 -*-
# @Time: 2020/10/12 10:23
# @Author: Lj
# @File: 530_二叉搜索树的最小绝对差.py

'''
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：中序遍历
'''
from leetcode.BinaryTree.NodeAndBuildTree import *

class Solution:
    #方法太繁琐，不好
    def getMinimumDifference(self, root: TreeNode) -> int:
        res_min = 1e5
        def single_root_min_difference(node):
            l_last = node.left if node.left else None
            r_last = node.right if node.right else None
            l_min, r_min = 1e5,1e5
            while l_last:
                if l_last.right:
                    l_last = l_last.right
                else:
                    l_min = abs(node.val - l_last.val)
                    break
            while r_last:
                if r_last.left:
                    r_last = r_last.left
                else:
                    r_min = abs(node.val - r_last.val)
                    break
            root_min = min(l_min, r_min)
            return root_min

        def trace(root):
            nonlocal res_min
            if not (root.left or root.right):
                return
            root_min = single_root_min_difference(root)
            res_min = min(res_min, root_min)
            if root.left:
                trace(root.left)
            if root.right:
                trace(root.right)
        trace(root)
        return res_min

    #参考答案
    

#测试
lst = [10,5,12,1,7]
root = list_buildTree(lst)
res = Solution().getMinimumDifference(root)
print(res)