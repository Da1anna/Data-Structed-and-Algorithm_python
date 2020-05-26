'''
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
最快速解法：哈希表
        1.遍历数组时，将数组中的数和位置存储到哈希表
        2.边遍历边查找，如果哈希表中有目标记录，则返回结果
'''

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        d = {}
        for i,num in enumerate(nums):
            #遍历一遍的关键代码：边记录数据边返回结果
            if target-num in d:
                return [d[target-num],i]
            d[num] = i
        return []
#测试
nums = [1,3,5,7]
res = Solution().twoSum(nums,8)
print(res)