
#链表节点定义,无空头节点
class ListNode:

    def __init__(self,x):
        self.val = x
        self.next = None

    #输出ListNode类本身
    def __str__(self) -> str:
        s = str(self.val)
        next = self.next
        while next:
            s += '->'+ str(next.val)
            next = next.next
        return s
#数组建立链表
def list_buildNode(arr:[int]) -> ListNode:
    head = ListNode(arr[0])
    cur = head
    for num in arr[1:]:
        node = ListNode(num)
        cur.next = node
        cur = node
    return head

#测试
arr = [1,2,3]
head = list_buildNode(arr)
# print(head.next)
