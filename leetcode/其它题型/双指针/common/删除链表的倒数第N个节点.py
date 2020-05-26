'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
快慢指针+删除链表节点：基本操作
'''
from leetcode.其它题型.双指针.ListNode import *
class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #特判：
        if not head:
            return head
        front = ListNode(-1)
        front.next = head
        p,q = front,front
        #定位
        while q.next:
            q = q.next
            n -= 1
            if n < 0:
                p = p.next
        #删除
        p.next = p.next.next
        # cur = p.next
        # tmp = cur.next
        # p.next = tmp

        return front.next

#测试
nums = [1,2,3,4,5]
head = list_buildNode(nums)
res = Solution().removeNthFromEnd(head,5)
print(res)

