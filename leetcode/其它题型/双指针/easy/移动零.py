'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    #暴力法
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        # print(nums)

    #双指针，一左一右，两边夹击。     DIY:太慢了！
    def moveZeroes_2(self, nums: [int]) -> None:

        pre,post = 0,len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                pre = i
                break
            pre = i
        for j in range(len(nums)-1,-1,-1):
            if nums[j] != 0:
                post = j
                break
            post = j
        if pre >=  post:
            print(nums)
            return
        while pre < post:
            nums[pre],nums[post] = nums[post],nums[pre]
            post -= 1
            while nums[post] == 0:
                tmp = post
                while nums[post+1] != 0:
                    nums[post],nums[post+1] = nums[post+1],nums[post]
                    post +=1
                post = tmp
                post -= 1
        print(nums)

    #双指针，都从左边开始。  参考答案
    def moveZeroes_3(self, nums: [int]) -> None:
        p,q = 0,1
        while q < len(nums):
            if nums[p] == 0 and nums[q] != 0:
                nums[p],nums[q] = nums[q],nums[p]
            if nums[p] != 0:
                p += 1
            q += 1
        print(nums)
#测试
nums = [4,2,4,0,0,3,0,5,1,0]

Solution().moveZeroes_3(nums)
