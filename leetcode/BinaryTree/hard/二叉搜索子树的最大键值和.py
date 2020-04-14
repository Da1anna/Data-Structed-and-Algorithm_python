'''
1373. 二叉搜索子树的最大键值和
给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

二叉搜索树的定义如下：

任意节点的左子树中的键值都 小于 此节点的键值。
任意节点的右子树中的键值都 大于 此节点的键值。
任意节点的左子树和右子树都是二叉搜索树。


示例 1：

输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
输出：20
解释：键值为 3 的子树是和最大的二叉搜索树。

示例 2：

输入：root = [4,3,null,1,2]
输出：2
解释：键值为 2 的单节点子树是和最大的二叉搜索树。

示例 3：

输入：root = [-4,-2,-5]
输出：0
解释：所有节点键值都为负数，和最大的二叉搜索树为空。

示例 4：

输入：root = [2,1,3]
输出：6
示例 5：

输入：root = [5,4,8,3,null,6,3]
输出：7

'''

from leetcode.BinaryTree.NodeAndBuildTree import *


class Solution:
    def maxSumofBST(self,root:TreeNode) -> int:
        self.maxSum = 0
        self.postOrder_helper(root)
        return self.maxSum

    def postOrder_helper(self,root):
        #返回3各变量：以当前节点为根节点的BST树的和、树的最小的值、最大值
        if not root:
            return 0, 5e4, -5e4     #最大值和最小值？
        sum_l,min_l,max_l = self.postOrder_helper(root.left)
        sum_r,min_r,max_r = self.postOrder_helper(root.right)

        #判断是否为BST
        if root.val > max_l and root.val < min_r:
            self.maxSum = max(self.maxSum,root.val + sum_l + sum_r)
            return root.val + sum_l + sum_r,min(root.val,min_l),max(root.val,max_r)
        return root.val,-5e4,5e4

#测试
root_lst = [1,4,3,2,4,2,5,None,None,None,None,None,None,4,6]
root = list_buildTree(root_lst)
# print(root)

res = Solution().maxSumofBST(root)
print(res)