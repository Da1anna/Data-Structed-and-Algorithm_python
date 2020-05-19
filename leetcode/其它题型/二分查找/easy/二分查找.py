'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    #递归版
    def search_1(self, nums: [int], target: int) -> int:

        def helper(l,h,target) -> int:
            if l > h:
                return -1

            mid = (l + h)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return helper(l,mid-1,target)
            else:
                return helper(mid+1,h,target)
        l,h = 0,len(nums)-1
        return helper(l,h,target)

    #循环版
    def search_2(self, nums: [int], target: int) -> int:

        l,h = 0,len(nums)-1
        while (l <= h):
            mid = (l+h)//2
            if target == nums[mid]:
                break
            elif target < nums[mid]:
                h = mid - 1
            else:
                l = mid + 1

        return (l+h)//2 if l<=h else -1
#测试
nums = [-1,0,3,5,9,12]
res = Solution().search_2(nums,12)
print(res)