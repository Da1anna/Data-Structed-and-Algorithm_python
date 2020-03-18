'''
1.根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder:list, inorder:list) -> TreeNode:
        if len(inorder) == 0:
            return None
        #前序遍历第一个为根节点
        root = TreeNode(preorder[0])
        #在中序序列中找到划分根节点划分左右子树的位置
        mid = inorder.index(preorder[0])
        #递归的构建左子树
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        #递归的构建右子树
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root


'''
2.给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        res = []
        #利用队列来辅助储存每一层的节点
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(tmp)
        return res

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

'''
#递归版
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        return [root.val] + self.postorderTraversal(root.left) + self.postorderTraversal(root.right)

#迭代版


































