'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
思路一：在一条链表上解决问题
      1.用双指针分别定位到目标位置
      2.循环重组链表

大神思路：用两个空链表分别接收head上的满足条件的值
        再拼接链表      
'''
from leetcode.其它题型.双指针.ListNode import *

class Solution:

    #思路一：逻辑复杂一点
    def partition(self, head: ListNode, x: int) -> ListNode:
        #设置空头节点，便于写算法
        front = ListNode(0)
        front.next = head
        #分别找出（第一个大于等于 x 的节点）和（在x后面的第一个小于x的节点）的前一节点
        p,q = front,front
        while p.next:
            #定位p
            if p.next.val < x:
                p = p.next
            #p定位完成，定位q
            else:
                q = p.next
                while q.next and q.next.val >= x:
                    q = q.next
                break
        #特判
        if not p.next:
            return front.next
        #重组链表
        while q.next:
            if q.next.val < x:
                #重组
                last = p.next
                cur = q.next
                tmp = cur.next
                cur.next = last
                q.next = tmp
                p.next = cur
                #重组后，p节点后移，继续判断
                p = p.next
            # 若q节点后一位不小于x，则q后移，继续判断
            else:
                q = q.next
        return front.next

    #思路二:逻辑易懂，代码简洁
    def partition_2(self, head: ListNode, x: int) -> ListNode:
        listNode_1 = ListNode(-1)
        listNode_2 = ListNode(-1)
        p,q = listNode_1,listNode_2

        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next

        p.next = listNode_2.next
        q.next = None
        return listNode_1.next

#测试
arr = [1,4,2,5,3,2]
head = list_buildNode(arr)
res = Solution().partition_2(head,3)
print(res)