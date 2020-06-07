'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：1.字典统计次数
      2.建大顶堆
        要点：两个函数percUp和percDown
            percUp————对每一个非叶节点进行percDown
            percDown————将某一个节点向下调整到“合适”位置
      3.弹出k个堆顶值：（每弹一个就要维护堆）
'''
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:

        #从末位的第一个非叶节点开始，逐个进行percDown
        def percUp(lst):
            new_lst = [-1] + lst
            n = len(new_lst)-1
            for i in range(n//2,0,-1):
                percDown(new_lst,i)

            return new_lst
        #将某一位置的节点向下调整到合适的位置
        def percDown(lst, i):
            n = len(lst)-1
            j = 2*i
            while j <= n:
                if j+1 <= n and lst[j+1][1] > lst[j][1]:
                    j = j+1
                if lst[i][1] < lst[j][1]:
                    lst[i],lst[j] = lst[j],lst[i]
                    i = j
                    j = 2*i
                else:
                    break
        # 用字典统计数字的次数
        d_cnt = {}
        for a in nums:
            if a not in d_cnt:
                d_cnt[a] = 1
            else:
                d_cnt[a] += 1
        lst_cnt = list(d_cnt.items())
        print(lst_cnt)

        #建大顶堆
        heap = percUp(lst_cnt)
        #取前K个元素
        res = []
        for _ in range(k):
            heap[1],heap[-1] = heap[-1],heap[1]
            res.append(heap.pop()[0])
            percDown(heap,1)
        return res

#测试
nums = [1]
k = 1
res = Solution().topKFrequent(nums, k)
print(res)
