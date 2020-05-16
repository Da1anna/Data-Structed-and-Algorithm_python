'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    #
    def combinationSum3(self, k: int, n: int) -> [[int]]:

        nums = [i for i in range(1,10)]
        res = []
        def backtrack(i,path,n,k):
            #边界条件
            if n == 0 and k == 0:
                res.append(path[:])
                return

            for j in range(i,len(nums)):
                #选择
                if k > 0 and n - nums[j] >= 0:
                    path.append(nums[j])
                    backtrack(j+1,path,n - nums[j],k - 1)
                    #撤销选择
                    path.pop()

        backtrack(0,[],n,k)
        return res
#测试
res = Solution().combinationSum3(3,9)
print(res)