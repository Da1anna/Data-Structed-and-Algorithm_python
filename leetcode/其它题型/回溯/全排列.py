'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    #回溯
    def permute(self, nums: [int]) -> [[int]]:

        # 标准回溯算法框架
        def backtrack(nums, path, used):
            #边界条件
            if len(path) == len(nums):
                path_ = path[:]
                res.append(path_)
                return
            #for循环 + 递归
            for i in range(len(nums)):
                #做选择
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, path, used)
                    #撤销选择
                    path.pop()
                    used[i] = False

        used = [False for _ in nums]
        res = []
        backtrack(nums,[],used)
        return res

    #
#测试
nums = [1,2,3]
res = Solution().permute(nums)
print(res)



