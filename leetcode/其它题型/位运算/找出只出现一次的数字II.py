'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：
因为整数可以用一个32位的二进制表示，所以建立一个32位的数组
将nums中每个数的二进制上的1累加起来记录在bits上
因为只有一个数出现1次，其它出现3次，所以将bits的每一位上的数字%3，若那个数字在这一位没有贡献，则位0，否则为1
所以最后的二进制就是那个只出现了一次的数

注：这种解法只能应用于正整数，因为负数的二进制表示不一样    
'''
class Solution:
    def singleNumber(self, nums: [int]) -> int:

        bits = [0] * 32
        res = 0
        #这种循环的顺序是先对每一位上的数求出结果，再将结果组合起来就是那个数
        for i in range(32):
            for j in nums:
                bits[i] += (j >> i) & 1
            res |= (bits[i] % 3) << i
        return res

    #数学规律法
    def singleNumber_1(self, nums: [int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
#测试
nums = [3,2,2,2]
res = Solution().singleNumber(nums)
print(res)