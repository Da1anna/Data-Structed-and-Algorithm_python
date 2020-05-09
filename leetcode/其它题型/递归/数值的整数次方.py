'''
实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
 

说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    #超时
    #得用二进制的一些东西？
    def myPow(self, x: float, n: int) -> float:

        def helper(x,n) -> float:
            if n == 1:
                return x
            return helper(x,n//2) * helper(x,n - n//2)

        if x == 0 :
            if n > 0:
                return 0
            elif n == 0:
                return 1
            else:
                print("不可以")
        if n > 0:
            return helper(x,n)
        elif n < 0:
            return 1 / helper(x,-n)
        else:
            return 1

#测试
i = 0.00001
res = Solution().myPow(i,123456)
print(res)
