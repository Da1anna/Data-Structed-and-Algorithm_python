'''
棒球比赛计分
整数、C、D、+
'''
class Solution:
    def calPoints(self, ops: [str]) -> int:
        stack = []
        for c in ops:
            if c == "C":
                stack.pop()
            elif c == "D":
                stack.append(2*stack[-1])
            elif c == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(c))
        return  sum(stack)

'''
两个数组比较，找出最大值。。。
'''
class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        res = []
        for i in nums1:
            ind = nums2.index(i) + 1
            if ind == len(nums2) or max(nums2[ind:]) < i:
                res.append(-1)
                continue
            else:
                for j in nums2[ind:]:
                    if j == nums2[-1] and j <= i:
                        res.append(-1)
                    else:
                        if j > i:
                            res.append(j)
                            break
        return res
