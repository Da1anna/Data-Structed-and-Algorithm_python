'''
1.二叉树的节点表示
'''
class BinaryNode():
    def __init__(self,value=None):
        self.key = value
        self.left = None
        self.right = None

    def insertLeft(self, new_value):
        if self.left == None:
            self.left = BinaryNode(new_value)
        else:
            t = BinaryNode(new_value)
            t.left = self.left
            self.left = t

    def insertRight(self, new_value):
        if self.right == None:
            self.right = BinaryNode(new_value)
        else:
            t = BinaryNode(new_value)
            t.right = self.right
            self.right = t

    def get_leftnode(self):
        return self.left

    def get_rightnode(self):
        return self.right

    def setvalue(self,value):
        self.key = value

    def getvalue(self):
        return self.key
'''
测试

r = BinaryNode('a')
print(r.getvalue())
print(r.get_leftnode())
r.insertLeft('b')
print(r.get_rightnode())
print(r.get_leftnode().getvalue())
r.insertRight('c')
print(r.get_rightnode())
print(r.get_rightnode().getvalue())
r.get_rightnode().setvalue('hello')
print(r.get_rightnode().getvalue())

'''

'''
2.分析树
我们还可以表示诸如 （（7 + 3）*（5-2）） 数学表达式作为分析树
例题详情查看："https://facert.gitbooks.io/python-data-structure-cn/6.树和树的算法/分析树"

'''
from pythonds.trees.binaryTree import BinaryTree

def build_parseTree(fpexp):
    fplist = fpexp.split()
    #初始化:注意：这里的算术式样式是( 10 + 5 ) * ( 3 - 1 )
                            # 不是(( 10 + 5 ) * ( 3 - 1 ) )
    etree = BinaryTree('')
    etree.insertLeft('')
    cur_node = etree.getLeftChild()
    stack = []
    stack.append(etree)

    for char in fplist:
        if char == '(':
            cur_node.insertLeft('')
            stack.append(cur_node)
            cur_node = cur_node.getLeftChild()
        elif char not in ['+','-','*','/',')']:
            cur_node.setRootVal(int(char))
            parent = stack.pop()
            cur_node = parent
        elif char in ['+','-','*','/']:
            cur_node.setRootVal(char)
            cur_node.insertRight('')
            stack.append(cur_node)
            cur_node = cur_node.getRightChild()
        elif char == ')':
            parent = stack.pop()
            cur_node = parent
        else:
            print("有错误字符")
    return etree
# pt = build_parseTree("( 10 + 5 ) * ( 3 - 1 )")
# pt.preorder()

'''
3.树的遍历
'''
#3.1 前序遍历
def preorder(treeNode):
    if treeNode:
        print(treeNode.getvalue())
        preorder(treeNode.get_leftnode())
        # print(treeNode.getvalue())    #中序
        preorder(treeNode.get_rightnode())
        # print(treeNode.getvalue())    #后序

#3.2 层次遍历
def levelTrace(root:BinaryNode) -> [int]:
    if not root:
        return []
    queue = [root]
    res = []

    while queue:
        cur = queue.pop(0)
        res.append(cur.key)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return res

#测试

#将列表初始化到完全二叉树
lst = [3,9,20,None,None,15,7]
root = BinaryNode()

def listBuildTree(node:BinaryNode,lst,i):
    if i >= len(lst):
        return None
    node.key = lst[i]
    node.left = listBuildTree(BinaryNode(),lst,2*i+1)
    node.right = listBuildTree(BinaryNode(),lst,2*i+2)
    return node

listBuildTree(root,lst,0)
print(root.right.key)

#层次遍历
res = levelTrace(root)
print(res)


'''
4.基于二叉堆的优先队列
二叉堆的性质：完全二叉树 + 根节点值大于（小于）两个子节点值
完全二叉树可以用列表来实现，可以不用节点表示
'''
class BinHeap():

    def __init__(self):
        self.heapList = [0]
        self.curSize = 0

    def __str__(self):
        return ' '.join( str(i) for i in self.heapList[1:])

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
                i = i // 2
            else:
                break
    def insert(self,num):
        self.heapList.append(num)
        self.curSize += 1
        self.percUp(self.curSize)

    def percDown(self,i):
        j = 2*i
        while j <= self.curSize:
            if j+1 <= self.curSize and self.heapList[j+1] < self.heapList[j]:
                j += 1
            elif self.heapList[j] < self.heapList[i]:
                self.heapList[i],self.heapList[j]  = self.heapList[j],self.heapList[i]
                i = j
                j = 2*i
            else:
                break
    def buildHeap(self,alist):
        self.heapList += alist
        self.curSize = len(alist)
        for i in range(self.curSize//2,0,-1):
            self.percDown(i)
            print(self.heapList[1:])

    def delMin(self):
        minVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.curSize]
        self.heapList.pop()
        self.curSize -= 1
        self.percDown(1)
        return minVal


#测试

# bh = BinHeap()
# # bh.buildHeap([9,5,6,2,3])
# lst = [9,5,6,2,3]
# for num in lst:
#     bh.insert(num)
# print(bh)
#
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())



'''
5.二叉搜索树的实现
'''























