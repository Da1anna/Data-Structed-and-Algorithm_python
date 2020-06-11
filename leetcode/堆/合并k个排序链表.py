'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# class ListNode:
#
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def __lt__(self, other):
#         return self.val < other.val
from leetcode.其它题型.双指针.ListNode import *
import heapq as hp

class Solution:
    #这样写可行的原因是我们在ListNode里面重写了__lt__()函数，可以直接比较链表的大小，便于堆维护
    #但在leetcode上，链表无法重写比较函数，所以需要一点曲折
    def mergeKLists_1(self, lists: [ListNode]) -> ListNode:
        heap = lists
        hp.heapify(heap)
        head = ListNode(-1)
        res = head
        while heap:
            node = hp.heappop(heap)
            res.next = node
            res = res.next

            if node.next:
                hp.heappush(heap, node.next)
        return head.next

    #参考答案：heap的item是元组，元组的元素是node.val和链表的位置索引i
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                #这里heap里面放入的item是一个元组，元组间的比较是从元组的第一个元素开始依次比较
                #所以元组里面不能放入链表，因为若第一个元素相等，比较第二个元素链表时，无法比较
                hp.heappush(heap,(lists[i].val,i))

        head = ListNode(0)
        p = head
        while heap:
            val, idx = hp.heappop(heap)
            p.next = lists[idx]
            p = p.next
            lists[idx] = lists[idx].next


            if lists[idx]:
                hp.heappush(heap,(lists[idx].val,idx))
        return head.next



#测试
arr_1 = [1,4,5]
arr_2 = [1,3,4]
arr_3 = [2,6]

node_1 = list_buildNode(arr_1)
node_2 = list_buildNode(arr_2)
node_3 = list_buildNode(arr_3)

list_node = [node_1, node_2, node_3]
# print(list_node)
res = Solution().mergeKLists(list_node)
print(res)
