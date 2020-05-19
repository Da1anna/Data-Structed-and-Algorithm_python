'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    #这种写法逻辑不太好
    def searchInsert(self, nums: [int], target: int) -> int:
        l,h = 0,len(nums)-1
        while l < h:
            mid = (l + h)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
        if target <= nums[l]:
            return l
        else:
            return l+1


    #这个二分法是排除的思想，每次排除一部分区域，在内部不判断target的值是否找到了
    def searchInsert_2(self, nums: [int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return 0

        left = 0
        # 因为有可能数组的最后一个元素的位置的下一个是我们要找的，故右边界是 len
        right = size

        while left < right:
            mid = (left + right) // 2
            # 严格小于 target 的元素一定不是解
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                right = mid
        return left


#测试
nums = [1,3,5,6]
res = Solution().searchInsert_2(nums,7)
print(res)