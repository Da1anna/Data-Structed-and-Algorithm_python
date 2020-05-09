'''
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

 

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：

输入：n = 25
输出：1389537
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-th-tribonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:

    #记忆化递归
    def tribonacci_1(self, n: int) -> int:
        T = [0 for _ in range(n+1)]
        T[1],T[2] = 1,1
        def helper(n,T) -> int:
            if n == 0:
                return 0
            if T[n]:
                return T[n]
            T[n] =  helper(n-3,T) + helper(n-2,T) + helper(n-1,T)
            return T[n]

        return helper(n,T)

    #自底向上动态规划
    def tribonacci_2(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        x,y,z = 0,1,1
        for i in range(3,n+1):
            x,y,z = y,z,x+y+z
        return z
#测试
res = Solution().tribonacci_2(25)
print(res)