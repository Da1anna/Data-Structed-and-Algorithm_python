'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #特判
        if not head:
            return head
        if not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        q0,q1,q2 = dummy, head, head.next
        while True:
            q1.next = q2.next
            q2.next = q0.next
            q0.next = q2
            q1, q2 = q2, q1
            if q2.next:
                q1 = q2.next
                if q1.next:
                    q0 = q2
                    q2 = q1.next
                    continue
            break
        return dummy.next

    #代码优化版
    def swapPairs_1(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p0 = dummy
        while p0.next and p0.next.next:
            p1 = p0.next
            p2 = p1.next
            #两两交换
            p1.next = p2.next
            p2.next = p0.next
            p0.next = p2

            p0 = p1
        return dummy.next