# -*- coding:utf-8 -*-
# @Time: 2020/10/10 10:06
# @Author: Lj
# @File: 142_环形链表II.py

'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

进阶：
你是否可以不用额外空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：有数学题的感觉
    先通过快慢指针确定链表是否有环
    再根据数学知识，快指针走过的路程 - 慢指针 有特别的意义
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #快慢指针
        p,q = head,head
        hasCycle = False
        while p and p.next:
            p = p.next.next
            q = q.next
            if p == q:
                hasCycle = True
                break
        #有环，头节点和慢指针开始等速移动，相遇的节点即是环的入口
        if hasCycle:
            p = head
            while p != q:
                p = p.next
                q = q.next
            return p
        else:
            return None