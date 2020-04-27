'''
515. 在每个树行中找最大值
您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]
'''
from leetcode.BinaryTree.NodeAndBuildTree import *


class Solution:
    def largestValues(self, root: TreeNode) -> [int]:
        #层次遍历中求出每一层的最大值
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            n = len(queue)
            level_max = -1e9    #-1x10的9次方，还不够小
            for _ in range(n):
                cur = queue.pop(0)
                level_max = max(level_max,cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level_max)
        return res

#测试
lst = [1,3,2,5,3,None,9]
root = list_buildTree(lst)

res = Solution().largestValues(root)
print(res)