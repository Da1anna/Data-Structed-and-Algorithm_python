'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
思路：先用快慢指针找到链表中点，再反转链表，遍历比较
难点 1.想到反转链表
    2.实现反转链表
'''
from leetcode.其它题型.双指针.ListNode import *
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        #特判：
        if not head:
            return True
        #快慢指针找中点:奇偶不影响
        p,q = head,head
        while q and q.next:
            p = p.next
            q = q.next.next
        #反转链表,重点
        last = p
        cur = p.next
        while cur:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp
        p.next = None
        #比较
        while last:
            if head.val != last.val:
                return False
            head = head.next
            last = last.next
        return True

#测试
nums = [1,2,3,4,5,3,2,1]
head = list_buildNode(nums)
res = Solution().isPalindrome(head)
print(res)
