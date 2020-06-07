'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

进阶：
你是否可以不用额外空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from leetcode.其它题型.双指针.ListNode import *

'''
思路1：哈希表存储链表上的值，若重复，则是环的位置

思路2：快慢指针不仅可以判断是否有环，还可以定位环的位置
        当然需要一点数学上的计算，通过设p,q指针第一次相遇的距离之间的关系，计算过程见参考答案
'''
class Solution:
    #哈希表记录遍历过的节点，需要线性额外空间
    def detectCycle(self, head: ListNode) -> ListNode:
        d = {}
        pos = 0
        while head:
            if head not in d:
                d[head] = pos
                pos += 1
            else:
                return head
            head = head.next
        return None

    #快慢指针
    #不用额外空间指的是O（1）空间
    def detectCycle_1(self, head: ListNode) -> ListNode:
        p, q = head, head
        while True:
            if not q or not q.next:
                return None
            p, q = p.next, q.next.next
            if p == q:
                break
        #第一次相遇后，将q定位到head,pq都以步伐1移动，再次相遇时，即是入环的位置
        q = head
        while q != p:
            p, q = p.next, q.next
        return q
