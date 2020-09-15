
#简单级别
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
# print(climbStep_memo(10))



#中等级别
'''
1.最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

注：这个题在经典例题里有
'''
def LIS(lst:list) -> int:
    dp = [1 for _ in range(len(lst))]
    for i in range(1,len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                #dp[i]存储的是以当前数字结束的子序列的最长长度
                dp[i] = max(dp[i],dp[j] + 1)

    return max(dp)

#测试
lst = [10,9,2,5,3,7,101,18]
# print(LIS(lst))

'''
2.最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def minPath(grid:[[]]) -> int:
    m = len(grid)
    n = len(grid[0])
    # grid = grid

    for i in range(m):
        for j in range(n):
            if i == j == 0:
                continue
            elif i == 0:
                grid[i][j] = grid[i][j-1] + grid[i][j]
            elif j == 0:
                grid[i][j] = grid[i-1][j] + grid[i][j]
            else:
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
    print(grid)
    return grid[m-1][n-1]
grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1],
]
# print(minPath(grid))

'''
3.不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def sumOfpath(m,n) -> int:
    if m == n == 0:
        return 0
    if m == 1 or n == 1:
        return 1

    # dp = [[1]*n for _ in range(m)]      #这种初始dp的方式可能不太好
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

#测试
# print(sumOfpath(7,3))

'''
4.剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def cutRoap(n) -> int:
    dp = [0]*(n+1)
    dp[2] = 1

    for i in range(3,n+1):
        for j in range(1,i):
            #在3种情况下选择最大值：
            #1.选择不切j 2.只切j 3.切j后继续切，dp[i-j]表示i-j段继续切的最大乘积
            dp[i] = max(dp[i], (i-j)*j, j*dp[i-j])
    print(dp)
    return dp[-1]

#测试
# print(cutRoap(10))








