'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：按照大小顺序，找下一个全排列，可以将全排列看作一个数，找下一个大的数，这样比较好理解
      例如1234765，下一个大的数是1235467，寻找过程从右向左找，将一个降序的数4和比4大一点的5找出来，当然
       这个比4大的5必须在765这一段位置找，即是在降序4的升序段中找，再将45位置交换，再将5后面的数字按照升序排列
       就得到结果
'''

class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #从右向左找第一个降序的位置
        minor = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] <= nums[i-1] and i-1 >= 0:
                continue
            if i == 0:
                #此时排列是最大的，应对应最小排列
                nums.sort()
                print(nums)
                return
            minor = i-1
            break
        #从右向左找第一个大于“目标数（minor位置的数）”的数
        major = 0
        for j in range(len(nums)-1,minor,-1):
            if nums[j] > nums[minor]:
                major = j
                break
        #交换
        nums[minor],nums[major] = nums[major],nums[minor]
        #对minor位置后面的段升序排序，用了冒泡
        for _ in range(len(nums) - minor-1):
            for k in range(minor+1,len(nums)-1):
                if nums[k] > nums[k+1]:
                    nums[k],nums[k+1] = nums[k+1],nums[k]
        print(nums)

#测试
nums = [5,1,1]
Solution().nextPermutation(nums)

