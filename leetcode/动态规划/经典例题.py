'''
1.斐波那契数列的三种计算
1,1,2,3,5,8,13,21,34,55,89...
'''

#1.1 递归
def Fibonacci_R(i):
    if i in [1,2]:
        return 1
    return Fibonacci_R(i-1) + Fibonacci_R(i-2)

#1.2 备忘录
s = [-1] * 100
def Fibonacci_memo(i):
    if i in [1,2]:
        s[i] = 1
        return s[i]
    if s[i] != -1:
        return s[i]
    s[i] = Fibonacci_memo(i-1) + Fibonacci_memo(i-2)
    return s[i]

#1.3 动态规划？
def Fibonacci_D(n):
    s = [-1] * 100
    s[1],s[2] = 1,1
    if n > 2:
        for j in range(3,n+1):
            s[j] = s[j-1] + s[j-2]
    return s[n]

#测试
# for i in range(1,50):
#     print(Fibonacci_D(i),end=' ')


'''
2.最大连续子序列和（同easy中的一道习题）
'''
def maxSubArray_D2(lst:list) -> int:
    #上一个的简化版
    tmp = lst[0]
    max_ = tmp

    for num in lst[1:]:
        tmp = max(tmp + num,num)
        max_ = max(max_,tmp)
    return max_

'''
3.数塔问题
要求从顶层走到底层，若每一步只能走到相邻的结点，则经过的结点的数字之和最大是多少？
'''
#动态规划
data = [
        [9],
        [12,15],
        [10,6,8],
        [2,18,9,5],
        [19,7,10,4,16],
        ]

def numberTower(data:list) -> int:
    for i in range(len(data)-2,-1,-1):  #从倒数第二层开始遍历往回走
        for j in range(i+1):    #遍历当前层的数组
            data[i][j] = max(data[i+1][j],data[i+1][j+1]) + data[i][j]
    return data[0][0]


#测试
# print(numberTower(data))

'''
4. 01背包问题
有N件物品和一个容量为S的背包。第i件物品的费用是w[i]，价值是v[i]。求解将哪些物品装入背包可使价值总和最大。

例：N=5，S=9，w=[0,6,4,2,4,3],v=[0,8,6,3,5,5]
'''

def bagFor_maxV(N,S,w:list,v:list) -> int:

    # dp = [[0 for _ in range(S+1)] for _ in range(N+1)]    #可行
    dp = [[0]*(S+1) for _ in range(N+1)]      #可行
    # dp = [[0]*(S+1)]*(N+1)      #不可行，why?

    for i in range(1,N+1):
        for j in range(1,S+1):
            if j >= w[i]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]] + v[i])
            else:
                dp[i][j] = dp[i-1][j]
    #求放入了哪些物品
    j = S
    res = []
    for i in range(N,0,-1):
        if dp[i][j] > dp[i-1][j]:
           res.append(i)
           j -= w[i]
    print(res)

    return dp[N][S]

#测试
N=5
S=9
w=[0,6,4,2,4,3]
v=[0,8,6,3,5,5]
# print(bagFor_maxV(N,S,w,v))


'''
5.最长递增子序列(LIS)
给定一个序列 An = a1 ,a2 ,  ... , an ，找出最长的子序列使得对所有 i < j ，ai < aj 。
示例:

输入: 
[10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 
[2,3,7,101]，[2,5,7,101],[2,3,7,18],等等
它的长度是 
4
'''

def LIS(lst:list) -> int:
    k = len(lst)
    dp = [1 for _ in range(k)]

    for i in range(1,k):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i],dp[j]+1)
    #找出是哪些子序列
    #不会！
    # print(dp)
    return max(dp)

#测试
lst = [1,3,6,7,9,4,10,5,6]
print(LIS(lst))

'''
6.最长公共子序列(LCS)
一个序列 S ，如果分别是两个或多个已知序列的子序列，且是所有符合此条件序列中最长的，则 S 称为已知序列的最长公共子序列。
例如：
s1={1,3,4,5,6,7,7,8},s2={3,5,7,4,8,6,7,8,2}
输出：{3,4,6,7,8}
'''

def LCS(a:list,b:list) -> int:
    a1 = [0] + a
    b1 = [0] + b
    k1 = len(a1)
    k2 = len(b1)
    dp = [[0] * (k2) for _ in range(k1)]

    for i in range(1,k1):
        for j in range(1,k2):
            if a1[i] == b1[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    #如何列出最长公共子序列？

    return dp[-1][-1]

#测试
a = [1,2,5,3,1]
b = [2,1,5,1]
# print(LCS(a,b))




















