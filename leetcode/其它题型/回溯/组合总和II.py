'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：与上题相比，主要有两个区别：1，有重复数字；2，一个组合中不可重复使用同一个数字

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        #简洁经典版框架
        def backtrack(i, path, tar):
            if tar == 0:
                res.append(path[:])
                return
            for j in range(i,len(nums)):
                #选择（决策）
                if tar - nums[j] >= 0 :      #还未凑满并且当前值还没用过
                    #剪枝
                    if j > i and nums[j] == nums[j-1] :  #剪枝：去除相同数字的重复组合
                        continue

                    path.append(nums[j])
                    backtrack(j+1, path, tar - nums[j])       #传参要仔参悟每个参数的意义
                    #撤销（恢复）
                    path.pop()

        nums = sorted(candidates)
        tar = target
        res = []
        backtrack(0,[],tar)

        return res

#测试
nums = [4,1,1,4,4,4,4,2,3,5]

target = 10
res = Solution().combinationSum2(nums,target)
print(res)

