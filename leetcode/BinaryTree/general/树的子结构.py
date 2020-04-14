'''
面试题26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
'''
from leetcode.BinaryTree.NodeAndBuildTree import *

class Solution:
    def isSubStructure(self, a: TreeNode, b: TreeNode) -> bool:
        # 判断两个根节点相同的树是否是一个的子树
        def recur(a,b) -> bool:
            #边界条件
            if b == None:
                return True
            if a == None or a.val != b.val:
                return False
            #返回值+递归体
            return recur(a.left,b.left) and recur(a.right,b.right)
        #特殊情况处理
        if a is None or b is None:
            return False
        #分情况处理
        if a.val == b.val:
            return recur(a,b)
        return self.isSubStructure(a.left,b) or self.isSubStructure(a.right,b)

#测试
a_lst = [3,4,5,1,2]
b_lst = [4,1]
a = list_buildTree(a_lst)
b = list_buildTree(b_lst)
res = Solution().isSubStructure(a,b)
print(res)