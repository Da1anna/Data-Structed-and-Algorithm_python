'''
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
有问题，没写出来
'''
from leetcode.BinaryTree.NodeAndBuildTree import *

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        start = root
        #定位
        while root:
            if root.val == key:
                break
            root = root.left if key < root.val else root.right
        if not root:
            return start
        #删除
        tar_node = root
        if root.left:
            if root.left.right:
                pre = root.left
                cur = pre.right
                while cur.right:
                    cur = cur.right
                    pre = pre.right
                tar_node.val = cur.val
                pre.right = None
            else:
                tar_node.val = root.left.val
                root.left = None
            return start
        if root.right:
            if root.right.left:
                pre = root.right
                cur = pre.left
                while cur.left:
                    cur = cur.left
                    pre = pre.left
                tar_node.val = cur.val
                pre.left = None
            else:
                tar_node.val = root.right.val
                root.right = None
            return start
        #叶子节点的情况
        root = None     #为啥这种写法不行？
        return start

#测试
lst = [5,3,6,2,4,None,7]
root = list_buildTree(lst)

res = Solution().deleteNode(root,5)
def levelTrace(root) -> [int]:
    if not root:
        return []
    queue = [root]
    res = []

    while queue:
        cur = queue.pop(0)
        res.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return res

ans = levelTrace(res)
print(ans)



