'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。

示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3],
函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：双指针，i:遍历数组，j:待覆盖的位置
    
'''
class Solution:

    #参考答案：非常规思维，比较难想到
    def removeDuplicates(self, nums: [int]) -> int:
        j,count = 1,1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1

            '''
            这一步比较难理解
            若count > 2,则继续遍历，直到找到新值，来覆盖j上的重复两次以上的值
            属于反向思维
            
            若正向思维，直接处理count > 2的情况，用j来覆盖i,那么j不好定位
            且返回值不好确定，因为i成了返回值，但i是要遍历完数组的
            '''
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j

#测试
nums = [0,0,1,1,1,1,2,2,3]
res = Solution().removeDuplicates(nums)
for a in nums[:res]:
    print(a,end=' ')