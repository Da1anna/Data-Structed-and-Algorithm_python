# -*- coding:utf-8 -*-
# @Time: 2020/10/3 10:38
# @Author: Lj
# @File: 1_两数之和.py

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    #暴力法  O(n2)
    def twoSum(self, nums: [int], target: int) -> [int]:
        res = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res += [i,j]
                    return res

    #哈希法
    def twoSum_1(self, nums, target) -> [int]:
        d = {}
        res = []
        for i in range(len(nums)):
            if target-nums[i] in d:
                res += [d[target-nums[i]],i]
                return res
            d[nums[i]] = i
        return res

    #哈希法的代码优化版
    def twoSum_2(self, nums, target) -> [int]:
        d = {}
        for i,num in enumerate(nums):
            if target-num in d:
                return [d[target-num],i]
            d[num] = i
        return []

#测试
nums = [2,7,11,15]
target = 19

res = Solution().twoSum_2(nums, target)
print(res)

