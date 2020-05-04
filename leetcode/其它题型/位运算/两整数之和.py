'''
不使用运算符 + 和 - ，计算两整数a 、b之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
低位和高位
缺点：这种写法只能计算非负整数
对于负数，我还没搞太懂
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while True:
            low = a ^ b
            car = a & b
            if car == 0:
                return low
            a = low
            b = car << 1


#测试
res = Solution().getSum(3,5)
print(res)

