'''
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-k-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路1：堆排序，小顶堆，时间复杂度不好

思路2：用大顶堆

思路3：快排，当一侧满足K个数时，停止
        没太搞懂，这里没有写
'''

class Solution:

    #小顶堆
    def smallestK(self, arr: [int], k: int) -> [int]:
        #设计最小堆
        def percDown(arr,i):
            j = 2*i
            while j < len(arr):
                if j+1 < len(arr) and arr[j+1] < arr[j]:
                    j += 1
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
                    i = j
                    j = 2*i
                else:
                    break

        def percUp(arr):
            n = len(arr)-1
            for i in range(n//2,0,-1):
                percDown(arr,i)
        #建立最小堆
        arr.insert(0,-1)
        percUp(arr)
        #取前k个最小值
        res = []
        for _ in range(k):
            arr[1],arr[-1] = arr[-1],arr[1]
            res.append(arr.pop())
            percDown(arr,1)
        return res

    #大顶堆:因为heapq没有实现大顶堆，这里采用对数组元素取反的方法构建大顶堆，输出元素时再取反回来
    #不明白为啥在leetcode上有bug
    def smallestK_1(self, arr: [int], k: int) -> [int]:
        import heapq as hp

        heap = []
        for a in arr[:k]:
            hp.heappush(heap, -a)

        for b in arr[k:]:
            if b < -heap[0]:
                hp.heappushpop(heap,-b)

        res = []
        for c in heap:
            res.append(-c)

        return res

#测试
arr = [1,3,5,7,2,4,6,8]
k = 4
res = Solution().smallestK_1(arr, k)
print(res)