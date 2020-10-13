# -*- coding:utf-8 -*-
# @Time: 2020/10/4 10:38
# @Author: Lj
# @File: 2_两数相加.py

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 
的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        cur = l3
        p,q = l1,l2
        num_2 = 0

        while p and q:
            num = p.val + q.val + num_2
            num_1 = num%10
            num_2 = num//10
            cur.next = ListNode(num_1)
            cur = cur.next
            p = p.next
            q = q.next

        w = p if p else q   #获取还未遍历完的链表
        #处理一个链表的情况
        while num_2 and w:
            num = w.val + num_2
            w.val = num%10
            cur.next = ListNode(w.val)
            cur = cur.next
            num_2 = num//10
            w = w.next
        if w:
            cur.next = w
        if num_2:
            cur.next = ListNode(num_2)

        return l3.next

    #逻辑优化
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        cur = res
        carry = 0

        while l1 or l2:
            p1 = l1.val if l1 else 0
            p2 = l2.val if l2 else 0
            num = p1 + p2 + carry
            cur.next = ListNode(num%10)
            cur = cur.next
            carry = num//10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            cur.next = ListNode(carry)
        return res.next

#测试
def list_buildNode(lst):
    head = ListNode(0)
    q = head
    for num in lst:
        q.next = ListNode(num)
        q = q.next
    return head.next
lst1 = [2,4]
lst2 = [5,6,9,9,1]
l1 = list_buildNode(lst1)
l2 = list_buildNode(lst2)

res = Solution().addTwoNumbers_1(l1,l2)
while res:
    print(res.val,end='->')
    res = res.next




