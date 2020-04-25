from leetcode.BinaryTree.NodeAndBuildTree import *

'''
1.路径总和II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def pathSum2(root:TreeNode,sum_:int):
    res = []
    stack = [([root.val],root)]

    while stack:
        tmp,cur = stack.pop()
        if  not cur.left and not cur.right:
            if sum(tmp) == sum_:
                res.append(tmp)
        if cur.right :
            stack.append((tmp + [cur.right.val],cur.right))
        if cur.left :
            stack.append((tmp + [cur.left.val],cur.left))
    return res

#测试

# res = pathSum2(root,22)
# print(res)


'''
2.路径总和I
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#非递归解法：用栈实现先序遍历
def pathSum1_NR(root:TreeNode,sum_) -> bool:
    stack = [(root.val,root)]
    found = False

    while stack and not found:
        tmp,cur = stack.pop()
        if not cur.left and not cur.right:
            if tmp == sum_:
                found = True
        if cur.right:
            stack.append((tmp+cur.right.val,cur.right))
        if cur.left:
            stack.append((tmp+cur.left.val,cur.left))
    return found

#测试
# res = pathSum_NR(root,22)
# print(res)


'''
3.路径总和III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#双重递归
def pathSum3(root:TreeNode,sum_) -> int:
    #整棵树的每个节点都dfs一遍
    if not root:
        return 0
    return dfs(root,sum_) + pathSum3(root.left,sum_) + pathSum3(root.right,sum_)

def dfs(root,sum_):
    #从某一顶点开始的先序遍历
    if not root:
        return 0
    tmp = sum_ - root.val
    return (1 if tmp == 0 else 0) + dfs(root.left,tmp) + dfs(root.right,tmp)

#测试
lst=[10,5,-3,3,2,None,11,3,-2,None,1]
sum = 8
root = list_buildTree_2(lst)

res = pathSum3(root,sum)
print(res)