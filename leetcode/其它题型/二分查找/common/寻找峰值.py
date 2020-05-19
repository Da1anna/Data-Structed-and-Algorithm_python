'''
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    #通过，但效果不好，代码也冗长
    def findPeakElement(self, nums: [int]) -> int:

        def helper(l,h) -> int:
            #边界条件：
            if l > h:
                return -1

            mid = (l+h)//2
            pre = mid - 1
            post = mid + 1
            if pre == -1:
                if nums[mid] > nums[post]:
                    return mid
                else:
                    return helper(mid+1,h)
            if post == len(nums):
                if nums[mid] > nums[pre]:
                    return mid
                else:
                    return helper(l,mid-1)

            elif nums[pre] < nums[mid] > nums[post]:
                return mid

            left = helper(l,mid-1)
            right = helper(mid+1,h)
            return left if right == -1 else right

        #特判
        if len(nums) == 1:
            return 0
        #调用函数
        return helper(0,len(nums)-1)

    #参考答案
    def findPeakElement_2(self, nums: [int]) -> int:
        l,r = 0,len(nums) - 1
        while l < r:
            mid = (l + r)//2
            if nums[mid] < nums[mid+1]:     #说明mid后面一定有个峰值
                l = mid + 1
            else:                           #mid前面一定有个峰值
                r = mid
        return l
#测试
nums = [1,2]
res = Solution().findPeakElement_2(nums)
print(res)
