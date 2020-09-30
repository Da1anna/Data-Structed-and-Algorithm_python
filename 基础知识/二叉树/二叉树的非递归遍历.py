''''''
'''
二叉树的前、中、后序遍历的非递归写法
'''

'''前序遍历'''
def preorder(root) -> [int]:
    stack = [root]
    path = []

    while stack:
        cur = stack.pop()
        path.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return path


def inorder(root) -> [int]:
    stack = []
    path = []
    cur = root

    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            path.append(cur.val)
            cur = cur.right
    return path


def postorder(root) -> [int]:
    stack = []
    path = []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left if cur.left else cur.right
        cur = stack.pop()
        path.append(cur.val)
        if stack and stack[-1].left == cur:
            cur = stack[-1].right
        else:
            cur = None
    return path


from leetcode.BinaryTree.NodeAndBuildTree import *
if __name__ == "__main__":
    lst = [5,4,7,2,3]
    root = list_buildTree(lst)
    path = preorder(root)
    print(path)