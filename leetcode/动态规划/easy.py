'''
1. 最大连续子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

#1.1 蛮力
def maxSubArray(lst:list) -> int:
    max_ = -100
    for i in range(len(lst)):
        tmp = lst[i]
        for j in range(i+1,len(lst)):
            tmp += lst[j]
            max_ = max(max_,tmp)
    return max_

#1.1 动态规划
def maxSubArray_D(lst:list) -> int:
    tmp = lst[0]
    max_ = tmp

    for num in lst[1:]:
        if tmp + num > num:
            tmp = tmp + num
            max_ = max(max_,tmp)
        else:
            tmp = num
            max_ = max(max_,tmp)
    return max_

def maxSubArray_D2(lst:list) -> int:
    #上一个的简化版
    tmp = lst[0]
    max_ = tmp

    for num in lst[1:]:
        tmp = max(tmp + num,num)
        max_ = max(max_,tmp)
    return max_

#测试
# lst = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray_D2(lst))


'''
2. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

#2.1 动态规划
def climbStep(n:int) -> int:
    if n < 3:
        return n

    s = [0] * (n+1)
    s[1],s[2] = 1,2
    for i in range(3,n+1):
        s[i] = s[i-1] + s[i-2]
    return s[n]

#2.2 备忘录
s = [0] * 100
def climbStep_memo(n:int) -> int:
    if s[n] != 0:
        return s[n]
    if n in [1,2]:
        s[n] = n
        return s[n]
    s[n] = climbStep_memo(n-1) + climbStep_memo(n-2)
    return s[n]

#测试
print(climbStep_memo(10))


























