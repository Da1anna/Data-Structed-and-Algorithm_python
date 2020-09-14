# -*- coding:utf-8 -*-
# @Time: 2020/9/7 11:09
# @Author: Lj
# @File: 设计链表.py

'''
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。
val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，
则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#修改版
'''
一般来说，链表的题目，加一个dummy哑节点比较容易写代码，因为可以忽略head节点为空的情况
'''
class Node:

    def __init__(self,val:int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.length = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        # print(cur.val)
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index < 0:
            index = 0
        pre = self.head
        for _ in range(index):
            pre = pre.next
        node = Node(val)
        node.next = pre.next
        pre.next = node

        self.length += 1
        # print(self)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        pre = self.head
        for _ in range(index):
            pre = pre.next
        pre.next = pre.next.next

        self.length -= 1
        # print(self)

    def __str__(self):
        res = 'head'
        cur = self.head
        for _ in range(self.length):
            cur = cur.next
            res += '->{}'.format(str(cur.val))
        return res

# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()
linkedList.addAtHead(7)
linkedList.addAtHead(2)
linkedList.addAtHead(1)
linkedList.addAtIndex(3,0)
linkedList.deleteAtIndex(2)
linkedList.addAtHead(6)
linkedList.addAtTail(4)
linkedList.get(4)
linkedList.addAtHead(4)
linkedList.addAtIndex(5,0)
linkedList.addAtHead(6)




