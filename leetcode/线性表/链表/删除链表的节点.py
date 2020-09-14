# -*- coding:utf-8 -*-
# @Time: 2020/9/5 21:50
# @Author: Lj
# @File: 删除链表的节点.py

'''
剑指 Offer 18. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                return head
            pre = cur
            cur = cur.next
        return head

    #用哑节点
    def deleteNode_2(self, head: ListNode, val: int):
        dummy = ListNode(0)
        dummy.next = head
        if head.val == val:
            return head.next
        while head and head.next:   #如果head为空这里是不是会报错？
            if head.next.val == val:
                head.next = head.next.next
            head = head.next
        return dummy.next









































