'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：排序 + 双指针
'''
class Solution:

    #双指针：半DIY，通过
    def threeSum(self, nums: [int]) -> [[int]]:
        #特判
        if len(nums) < 3:
            return []
        #排序
        nums.sort()

        last= None
        res = []
        for i in range(len(nums)):
            if nums[i] != last:     #先对第一位去重
                l,r = i+1,len(nums)-1
                while l < r:
                    if nums[l] + nums[r] == -nums[i]:
                        res.append([nums[i],nums[l],nums[r]])
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < -nums[i]:
                        l += 1
                    else:
                        r -= 1
                last = nums[i]
        #未找到
        if not res:
            return []
        # print(res)

        #对l和r两个位置选出的结果去重
        j = 1
        for i in range(1,len(res)):
            if res[i] != res[i-1]:
                res[j] = res[i]
                j += 1
        return res[:j]

    #参考答案1:双指针————逻辑通顺，代码简洁
    def threeSum_1(self, nums: [int]) -> [[int]]:
        #特判：
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return res


#测试
nums = [-1, 0, 1, 2, -1, -4]

res = Solution().threeSum(nums)
print(res)
