'''
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from leetcode.BinaryTree.NodeAndBuildTree import *

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        #中序遍历二叉搜索树，形成有序数组
        def in_trace(root) -> list:
            if not root:
                return []
            return in_trace(root.left) + [root.val] + in_trace(root.right)
        lst = in_trace(root)

        #计算有序数组相邻元素的最小差值
        min_distance = 1e9
        for i in range(len(lst)-1):
            tmp = lst[i+1] - lst[i]
            min_distance = min(min_distance,tmp)
        return min_distance