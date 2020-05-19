'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：在二分查找框架下加一个情况处理
'''

class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        #l,h不是数组的下标，而是数组中数的可能范围
        l,h = 1,len(nums)-1
        while l < h:
            mid = (l + h)//2
            #用cnt记录小于等于mid这个数的数的个数
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            #二分区间的条件判断
            if cnt <= mid:
                l = mid + 1
            else:
                h = mid
        return l

#测试
nums = [3,1,2,3,6,4,5]
res = Solution().findDuplicate(nums)
print(res)