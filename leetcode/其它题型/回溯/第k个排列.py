'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
难点：如何早停
'''
class Solution:

    #设置k_参数，找出第个时，停止————这种写法也超出时间限制
    def getPermutation_1(self, n: int, k: int) -> str:

        nums = [str(i) for i in range(1,n+1)]
        res = []
        k_ = k
        def backtrack(nums, path):
            nonlocal k_
            if nums == []:
                res.append(path[:])
                k_ -= 1
                return
            for i in range(len(nums)):
                if k_ > 0:
                    backtrack(nums[:i]+nums[i+1:],path+nums[i])

        backtrack(nums,'')
        return  res[-1]

    #利用阶乘数来剪枝:成功
    #但代码不够简洁
    def getPermutation_2(self, n: int, k: int) -> str:

        nums = [str(i) for i in range(1, n + 1)]
        # 记录0到9的阶乘
        factorial = [1 for _ in range(n+1)]
        for i in range(2,n+1):
            factorial[i] = i * factorial[i-1]

        def backtrack(nums,path,k):
            #边界条件
            # if len(nums) == 0:    这种写法也可以，不过不好理解
            #     res.append(path[:])
            if len(nums) == 1:
                path += nums[0]
                res.append(path[:])
                return

            count = factorial[len(nums)-1]      #当前层的节点下面的总排列数
            for i in range(len(nums)):
                #剪枝
                if count < k:
                    k -= count
                    continue
                #找到位置，递归继续
                backtrack(nums[:i]+nums[i+1:],path+nums[i],k)
                #递归结束时，表示已找到目标排列，则后序不再遍历，不断退出循环
                break

        res = []
        backtrack(nums,'',k)
        return res[0]


#测试
res = Solution().getPermutation_2(3,3)
print(res)