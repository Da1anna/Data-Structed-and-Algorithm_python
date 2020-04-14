'''
树的节点定义和二叉树的初始化
'''

#1.节点定义
class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    # def  __str__(self):
    #     return ''.join(self.key)

#2.二叉树的初始化
#注：输入的序列一定按照完全二叉树的形式，没有值的地方填None，否则数组的索引对不上
def list_buildTree_2(lst:list, i=0) -> TreeNode:
    '''

    :param lst:
    :param i: 根节点在数组中的索引
    :return:
    '''
    if i >= len(lst):
        return TreeNode(None)   #这是修改部分，即使是空节点，也保持返回值和非空节点一致，都是TreeNode()
    node = TreeNode()
    node.val = lst[i]
    node.left = list_buildTree(lst, 2 * i + 1)
    node.right = list_buildTree(lst, 2 * i + 2)
    return node

def list_buildTree(lst:list, i=0) -> TreeNode:
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
    node.val = lst[i]
    node.left = list_buildTree(lst, 2 * i + 1)
    node.right = list_buildTree(lst, 2 * i + 2)
    return node


#测试
# if __name__ == "__main__":
#     lst = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
#     root = list_buildTree(lst)
#     print(root.left.left.left)
