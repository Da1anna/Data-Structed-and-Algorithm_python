# -*- coding:utf-8 -*-
# @Time: 2020/10/5 9:45
# @Author: Lj
# @File: 18_四数之和.py

'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存
在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    #借用三数和的思路
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c = b+1
                d = len(nums)-1
                while c < d:
                    num = nums[a]+nums[b]+nums[c]+nums[d]
                    if num == target:
                        tmp = [nums[a],nums[b],nums[c],nums[d]]
                        res.append(tmp)
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
                    elif num < target:
                        c += 1
                    else:
                        d -= 1
        return res

#测试
nums = [-2,-1,0,0,1,2]
res = Solution().fourSum(nums,0)
print(res)



