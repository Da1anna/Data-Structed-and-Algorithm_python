
''''''

'''
1.二叉树ADT的节点实现
'''
class BinaryTree():
    def __init__(self,value=None):
        self.key = value
        self.left = None
        self.right = None

    def insertLeft(self, new_value):
        if self.left == None:
            self.left = BinaryTree(new_value)
        else:
            t = BinaryTree(new_value)
            t.left = self.left
            self.left = t

    def insertRight(self, new_value):
        if self.right == None:
            self.right = BinaryTree(new_value)
        else:
            t = BinaryTree(new_value)
            t.right = self.right
            self.right = t

    def get_leftNode(self):
        return self.left

    def get_rightNode(self):
        return self.right

    def setValue(self,value):
        self.key = value

    def getValue(self):
        return self.key


#测试
# root = BinaryTree('a')
# root.insertLeft('b')
# root.insertRight('c')
# root.insertLeft('d')
# print(root.get_leftNode().getValue())



'''
2.分析树(解析树)
    2.1分析树的表示
        我们还可以表示诸如  fpexp='( 7 + 3 ) *( 5 - 2 )' 数学表达式作为分析树

        注意：注意表达式的最外层有无（），这影响算法的具体写法
'''

def build_parseTree(fpexp:str):
    fplist = fpexp.split()
    root = BinaryTree('')
    root.insertLeft('')
    root.insertRight('')
    stack = []
    cur = root
    stack.append(cur)
    cur = cur.get_leftNode()
    for c in fplist:
        if c == '(':
            cur.insertLeft('')
            cur.insertRight('')
            stack.append(cur)
            cur = cur.get_leftNode()
        elif c.isdigit():
            cur.setValue(c)
        elif c in ['+', '-', '*', '/']:
            cur = stack.pop()
            cur.setValue(c)
            stack.append(cur)
            cur = cur.get_rightNode()
        elif c == ')':
            cur = stack.pop()
        else:
            print('有错误字符')
            return
    return root

'''
    2.2分析树的计算
        计算分析树中所表示的数学表达式的结果
'''
import operator

def evaluate(parseTree):
    ops = {'+': operator.add, '-': operator.sub,
           '*': operator.mul, '/': operator.truediv}
    root = parseTree
    if root.getValue().isdigit():
        return int(root.getValue())

    leftC = root.get_leftNode()
    rightC = root.get_rightNode()
    fn = ops.get(root.getValue())
    return fn(evaluate(leftC), evaluate(rightC))


#测试
# parseTree = build_parseTree('( 4 + 3 ) * ( 5 - 2 )')
# res = evaluate(parseTree)
# print(res)

'''
3.树的遍历
    3.1 递归遍历
'''
#3.1 前序遍历：逐个打印
def preorder(treeNode):
    if treeNode:
        print(treeNode.key)
        preorder(treeNode.left)
        # print(treeNode.key)    #中序
        preorder(treeNode.right)
        # print(treeNode.key)    #后序

#输出为一个字符串
def inOrder(root):
    if not root:
        return ''
    return inOrder(root.left) + root.key + inOrder(root.right)


'''
    3.2 层次遍历： 用队列，不说明层次
'''
def levelTrace(root:BinaryTree) -> [int]:
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

'''
    3.3 前中后的非递归遍历
        用栈来实现
        见另一个.py文件 
'''


'''
将列表初始化到完全二叉树
    下面的2种方式有细微的差别：
        1是将数组中的None值存储在结点上，以致结点本身不为空，任然可以有子节点
        2是数组中的None值，在二叉树中表现为空结点
    两种构造方式导致二叉树的遍历会出现不同的结果

'''
def list_buildTree_1(lst:list,i=0):
    '''
    遇到空值时，本身节点的key为None，但节点不为None,叶节点的左右指针指向None,即叶节点的子节点为None
    这样的构造在某些条件判断下不好用，eg：if root.left:
    '''
    if i >= len(lst):
        return None
    node = BinaryTree()
    node.key = lst[i]
    node.left = list_buildTree_1(lst,2*i+1)
    node.right = list_buildTree_1(lst,2*i+2)
    return node

def list_buildTree_2(lst:list,i=0) -> BinaryTree:
    '''
    遇到空值时，本身节点为空，即父节点的左右指针指向None值
    这样的构造在遍历时不会打印None值
    '''
    if i >= len(lst):
        return None
    if lst[i] == None:
        return None
    node = BinaryTree()
    node.key = lst[i]
    node.left = list_buildTree_2(lst, 2 * i + 1)
    node.right = list_buildTree_2(lst, 2 * i + 2)
    return node


#测试
# lst = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
# root1 = list_buildTree_1(lst)
# root2 = list_buildTree_2(lst)
#
# #测试层次遍历
# res1 = levelTrace(root1)
# res2 = levelTrace(root2)
# print(res1,res2,sep="\n")


'''
4.基于二叉堆的优先队列
二叉堆的性质：完全二叉树 + 根节点值大于（小于）两个子节点值
完全二叉树可以用列表来实现，可以不用节点表示
'''

#书上大致思路
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
            if self.heapList[j] < self.heapList[i]:
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

    def delMin(self):
        minVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.curSize]
        self.heapList.pop()
        self.curSize -= 1
        self.percDown(1)
        return minVal

#DIY
class BinaryHeap():

    def __init__(self):
        self.lst = []

    def insert(self, k):
        self.lst.append(k)
        self._percUp(len(self.lst)-1)

    def findMin(self) -> int:
        return self.lst[0]

    def delMin(self) -> int:
        self.lst[0], self.lst[len(self.lst)-1] = \
            self.lst[len(self.lst)-1], self.lst[0]
        min = self.lst.pop()
        self._percDown(0)
        return min

    def isEmpty(self) -> bool:
        return self.size == 0

    def size(self) -> int:
        return len(self.lst)

    def buildHeap(self, lst:list):
        self.lst= lst
        last_parent = len(self.lst)//2 - 1
        for i in range(last_parent,-1,-1):
            self._percDown(i)

    def _percUp(self, i):
        cur = i
        parent = (cur-1)//2
        while parent >=0:
            if self.lst[cur] < self.lst[parent]:
                self.lst[cur], self.lst[parent] = self.lst[parent], self.lst[cur]
                cur = parent
                parent = (cur-1)//2
            else:
                break
    def _percDown(self, i):
        cur = i
        j = 2 * cur + 1
        while j < len(self.lst):
            if j+1 < len(self.lst) and self.lst[j+1] < self.lst[j]:
                j +=1
            if self.lst[j] < self.lst[cur]:
                self.lst[cur], self.lst[j] = self.lst[j], self.lst[cur]
                cur = j
                j = 2*cur+1
                continue
            else:
                break
    def __str__(self):
        return ' '.join(str(i) for i in self.lst)

#测试
# bh = BinHeap()
# bh.buildHeap([3,1,5,4,2,0,6])
# print(bh)
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh)
# bh.insert(-1)
# print(bh)


'''
5.堆排序
    思路：利用构建二叉堆的部分算法：
        1.将待排序数组看作完全二叉树的样子，从倒数第一个父节点开始，percDown
            直到首位；
        2.将首位（最小值）交换到末位，对首位（交换的末位）percDown，此时
            操作的数组不算上末位
        3.重复2，直到操作的数组长度为1
            
'''
def heap_sort(lst) -> list:
    l = len(lst)
    last_parent = l//2 - 1
    for i in range(last_parent, -1, -1):
        _percDown(lst, i, l)

    while l-1 > 0:
        lst[0], lst[l-1] = lst[l-1], lst[0]
        l -= 1
        _percDown(lst, 0, l)
    return lst[-1::-1]

def _percDown(lst, i, l):
    j = 2*i+1
    while j < l:
        if j+1 < l and lst[j+1] < lst[j]:
            j += 1
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
            i = j
            j = 2*i+1
        else:
            break


'''
6.二叉搜索树的实现

'''
#节点类
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left==self

    def isRightChild(self):
        return self.parent and self.parent.right==self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.left or self.right)

    def hasAnyChildren(self):
        return self.left or self.right

    def hasBothChild(self):
        return self.left and self.right

    def replaceNodeData(self,key,val):
        self.key = key
        self.val = val

#BST类
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    #增
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
            self.size += 1

    def _put(self,key,val,curNode):
        if key < curNode.key:
            if curNode.hasLeftChild():
                self._put(key,val,curNode.left)
            else:
                curNode.left = TreeNode(key,val,parent=curNode)
        else:
            if curNode.hasRightChild():
                self._put(key,val,curNode.right)
            else:
                curNode.right = TreeNode(key,val,parent=curNode)

    #查
    def get(self,key):
        resNode = self._get(key,self.root)
        if resNode:
            return resNode.val
        else:
            return None

    def _get(self,key,curNode):
        '''
        返回存储目标值的节点
        '''
        if not curNode:
            return None
        if key == curNode.key:
            return curNode
        elif key < curNode.key:
            return self._get(key,curNode.left)
        else:
            return self._get(key,curNode.right)

    #删除一个节点，很复杂，考虑情况比较多，暂时略
    def delete(self,key):
        pass

    def __len__(self):
        return self.size

    def __setitem__(self,key,val):
        self.put(key,val)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def __delitem__(self,key):
        self.delete(key)

#测试
# myBST = BinarySearchTree()
# myBST[4] = 'a'
# myBST[2] = 'b'
# myBST[1] = 'd'
# myBST[5] = 'c'
# myBST[3] = 'e'
# myBST[6] = 'f'
# myBST[7] = 'g'
# print(myBST[5])
# print(myBST[3])
# print(1 in myBST)


if __name__ == "__main__":
    lst = [5,4,3,7,2]
    root = list_buildTree_2(lst)

    res = preorder_NR(root)
    print(res)

























































