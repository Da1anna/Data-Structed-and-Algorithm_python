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


def list_buildTree(lst:list, i=0) -> TreeNode:
    '''
    这个构建更好
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

def BFS(root):
    queue = [root]
    res = []

    while queue:
        cur = queue.pop(0)
        res.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)

    print(res)

#测试
if __name__ == "__main__":
    lst = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
    root = list_buildTree(lst)
    BFS(root)
