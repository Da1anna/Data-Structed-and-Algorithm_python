'''
124. 二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
'''

from leetcode.BinaryTree.NodeAndBuildTree import *

class Solution:
    maxPathSum_ = -100

    def maxPathSum(self, root: TreeNode) -> int:
        self.postOrder_helper(root)
        return self.maxPathSum_

    def postOrder_helper(self,root):
        if not root:
            return 0
        #计算左边最大路径的值
        left = max(0,self.postOrder_helper(root.left))
        #计算右边最大路径的值
        right = max(0,self.postOrder_helper(root.right))
        #更新全局最值
        self.maxPathSum_ = max(self.maxPathSum_,left + right + root.val)
        #返回最大路径的值
        return max(left,right) + root.val

#测试
lst = [-10,9,20,None,None,15,7]
root = list_buildTree(lst)

res = Solution().maxPathSum(root)
print(res)


