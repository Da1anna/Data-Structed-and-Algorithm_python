# -*- coding:utf-8 -*-
# @Time: 2020/10/7 10:39
# @Author: Lj
# @File: 75_颜色分类.py

'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
经典的荷兰三色旗问题
用双指针，但具体的逻辑要仔细考虑
'''
class Solution:
    #计数排序
    def sortColors(self, nums: [int]) -> None:
        cnt_0, cnt_1, cnt_2 = 0, 0, 0
        for a in nums:
            if a == 0:
                cnt_0 += 1
            elif a == 1:
                cnt_1 += 1
            else:
                cnt_2 += 1
        for i in range(len(nums)):
            if cnt_0:
                nums[i] = 0
                cnt_0 -= 1
                continue
            if cnt_1:
                nums[i] = 1
                cnt_1 -= 1
                continue
            if cnt_2:
                nums[i] = 2
                cnt_2 -= 1

    #参考答案:双指针交换法
    def sortColors_1(self, nums: [int]) -> None:
        p0, p2 = 0, len(nums)-1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1


#测试
nums = [2,0,2,1,1,0]
Solution().sortColors_1(nums)
print(nums)


