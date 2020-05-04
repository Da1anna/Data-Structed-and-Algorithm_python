'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        #一般思路,时空都是O（n）
        dict = {}
        for a in nums:
            if a not in dict:
                dict[a] = 1
            else:
                dict[a] = dict.get(a) + 1
        for k,v in dict.items():
            if v == 1:
                return k
    def singleNumber_1(self, nums: [int]) -> int:
        #位异或运算：比较两个数的二进制，不同部分为1，相同部分为0
        #位与、位或、位异或可理解位二进制的‘逻辑运算’
        a = 0
        for i in nums:
            a ^= i
        return a

#测试
nums = [4,1,2,2,1]
res = Solution().singleNumber_1(nums)
print(res)


