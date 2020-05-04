'''
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：
先位异或运算，求出x和y的异或值
再用bitmask & (-bitmask)求出最右位的不同部分
再遍历nums,用位异或运算求出其中一个值：x
再求出y
'''
class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        #求x和y的异或
        bitmask = 0
        for i in nums:
            bitmask ^= i
        #寻找差异
        diff = bitmask & (-bitmask)     #-bitmask = ~bitmask + 1
        #求出x
        x = 0
        for i in nums:
            if i & diff:
                x ^= i
        return [x,bitmask^x]

#测试
nums = [1,4,3,3]
res = Solution().singleNumber(nums)
print(res)