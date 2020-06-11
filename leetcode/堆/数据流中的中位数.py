'''
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路1：最笨的方法，二分查找 + 插入排序
'''
#通过，时间击败35%
class MedianFinder_1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if self.size == 0:
            self.arr.append(num)
            self.size += 1
            return
        #二分查找，查找出num应该插入的位置
        left = 0
        right = self.size
        while left < right:
            mid = (left + right - 1)//2
            if num > self.arr[mid]:
                left = mid + 1
            else:
                right = mid

        self.arr.insert(left, num)
        self.size += 1

    def findMedian(self) -> float:
        if self.size%2 == 1:
            return self.arr[self.size//2]
        return (self.arr[self.size//2 - 1] + self.arr[self.size//2]) / 2.0


'''
思路2：两个堆（一大一小顶）
'''
#时间击败81%
import heapq as hp
class MedianFinder:

    def __init__(self):

        self.heap_l = []
        self.heap_s = []

    def addNum(self, num: int) -> None:
        #将相应元素压入相应堆
        if len(self.heap_l) == len(self.heap_s):
            hp.heappush(self.heap_s, num)
            top = hp.heappop(self.heap_s)
            hp.heappush(self.heap_l, -top)
        else:
            hp.heappush(self.heap_l, -num)
            top = -hp.heappop(self.heap_l)
            hp.heappush(self.heap_s, top)

    def findMedian(self) -> float:
        if len(self.heap_l) == len(self.heap_s):
            return (-self.heap_l[0] + self.heap_s[0]) / 2.0
        return -self.heap_l[0]

#测试
obj = MedianFinder()
arr = [1,2,3,4,5,6]
for num in arr:
    obj.addNum(num)
res = obj.findMedian()
print(res)
