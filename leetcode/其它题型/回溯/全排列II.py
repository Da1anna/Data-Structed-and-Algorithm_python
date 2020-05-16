'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:

        def backtrack(nums,path,res,used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                #选择
                if not used[i]:
                    #剪枝:先排序后，就可以这样写
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue

                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums,path,res,used)
                    #撤销选择
                    path.pop()
                    used[i] = False

        used = [False for _ in nums]
        res = []
        nums.sort()
        backtrack(nums,[],res,used)
        return res
#测试
nums = [1,1,2]
res = Solution().permuteUnique(nums)
print(res)