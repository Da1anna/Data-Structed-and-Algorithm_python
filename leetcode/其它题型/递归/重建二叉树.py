'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from leetcode.BinaryTree.NodeAndBuildTree import *

class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:

        def helper(preorder,inorder) -> TreeNode:
            #边界条件
            if inorder == []:
                return None
            #函数体处理
            root_val = preorder.pop(0)
            root_index = inorder.index(root_val)
            left = inorder[:root_index]
            right = inorder[root_index+1:]

            root = TreeNode(root_val)

            #改变参数，分治递归
            root.left = helper(preorder,left)
            root.right = helper(preorder,right)
            #返回值
            return root

        return helper(preorder,inorder)


#测试
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

res = Solution().buildTree(preorder,inorder)
print(res.right.left.val)