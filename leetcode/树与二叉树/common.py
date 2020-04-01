#树的节点定义和二叉树的初始化
#1.节点定义
class TreeNode():
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None

    # def  __str__(self):
    #     return ''.join(self.key)

#2.二叉树的初始化
#注：输入的序列一定按照完全二叉树的形式，没有值的地方填None，否则数组的索引对不上
def list_buildTree(lst:list,i=0) -> TreeNode:
    '''

    :param lst:
    :param i: 根节点在数组中的索引
    :return:
    '''
    if i >= len(lst):
        return TreeNode(None)   #这是修改部分，即使是空节点，也保持返回值和非空节点一致，都是TreeNode()
    node = TreeNode()
    node.key = lst[i]
    node.left = list_buildTree(lst,2*i+1)
    node.right = list_buildTree(lst,2*i+2)
    return node

def list_buildTree_2(lst:list,i=0) -> TreeNode:
    '''
    这个构建更好
    :param lst:
    :param i:
    :return:
    '''
    if i >= len(lst):
        return None
    if lst[i] ==None:
        return None
    node = TreeNode()
    node.key = lst[i]
    node.left = list_buildTree_2(lst, 2 * i + 1)
    node.right = list_buildTree_2(lst, 2 * i + 2)
    return node

#测试
lst = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
root = list_buildTree_2(lst)
# print(root.left.left.left.left)



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
def f(root:TreeNode,sum_:int):
    res = []
    stack = [([root.key],root)]

    while stack:
        tmp,cur = stack.pop()
        if  not cur.left and not cur.right:
            if sum(tmp) == sum_:
                res.append(tmp)
        if cur.right :
            stack.append((tmp + [cur.right.key],cur.right))
        if cur.left :
            stack.append((tmp + [cur.left.key],cur.left))
    return res

#测试

# res = f(root,22)
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

def pathSum1(root:TreeNode,sum_) -> bool:
    stack = [(root.key,root)]
    found = False

    while stack and not found:
        tmp,cur = stack.pop()
        if not cur.left and not cur.right:
            if tmp == sum_:
                found = True
        if cur.right:
            stack.append((tmp+cur.right.key,cur.right))
        if cur.left:
            stack.append((tmp+cur.left.key,cur.left))
    return found

#测试
res = pathSum1(root,22)
print(res)





