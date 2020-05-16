'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def combinationSum_1(self, candidates: [int], target: int) -> [[int]]:
        #未剪枝
        def backtrack(nums, path, tar):
            if sum(path) > tar:
                return
            elif sum(path) == tar:
                res.append(path[:])
                return
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[i:], path, tar)
                path.pop()

        nums = candidates
        res = []
        tar = target
        backtrack(nums, [], tar)

        return res

    def combinationSum_2(self, candidates: [int], target: int) -> [[int]]:
        #剪枝，加速
        def backtrack(i, path, tar):
            if tar == 0:
                res.append(path[:])
                return
            for j in range(i,len(nums)):
                #利用变量tar纪录每次选择前的差量，来判断选择与否
                if tar - nums[j] >= 0:
                    path.append(nums[j])
                    backtrack(j, path, tar - nums[j])
                    path.pop()

        nums = candidates
        res = []
        tar = target
        backtrack(0, [], tar)

        return res

#测试
candidates = [2,3,5]
target = 8

res = Solution().combinationSum_2(candidates,target)
print(res)

