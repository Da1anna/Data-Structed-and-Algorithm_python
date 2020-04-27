'''
面试题 04.12. 求和路径
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

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

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
提示：

节点总数 <= 10000
'''

from leetcode.BinaryTree.NodeAndBuildTree import *

class Solution:
    count = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        #层次遍历
        queue = [root]
        while queue:
            cur = queue.pop(0)
            self.preorder_helper(cur,sum)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return self.count

    def preorder_helper(self,root,sum):
        if not root:
            return
        if sum == root.val:
            self.count += 1
        self.preorder_helper(root.left,sum - root.val)
        self.preorder_helper(root.right,sum - root.val)

#测试
# lst = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
lst = [1,-2,-3,1,3,-2,None,-1]
root = list_buildTree(lst)

res = Solution().pathSum(root,-1)
print(res)