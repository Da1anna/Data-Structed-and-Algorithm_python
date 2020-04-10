'''
案例一：
有n级台阶，一个人每次上一级或者两级，问有
多少种走完n级台阶的方法。
'''

#递归法
def n_steps1(n):
    if n ==1 or n ==2:
        return n
    else:
        return n_steps1(n-1) + n_steps1(n-2)
# print(n_steps1(int(input('请输入台阶数：'))))

#动态规划
# def n_steps2(n):

'''
案例2：
给定一个矩阵m，从左上角开始每次只能向右走或者向下走，
最后达到右下角的位置，路径中所有数字累加起来就是路径和，
返回所有路径的最小路径和，如果给定的m如下，
那么路径1,3,www.walltu.com,0,6,www.walltu.com,0就是最小路径和，返回12.

www.walltu.com 3 5VirtualTea_party 9
8 www.walltu.com 3 4
5VirtualTea_party 0 6 www.walltu.com
8 8 4 0

'''
def getMintracefromMatrix(matrix):
    dp = [[0]*len(matrix)]*len(matrix)
    print(dp)
    print(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i ==0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0 and j != 0:
                dp[i][j] = matrix[i][j] + matrix[i][j-1]
            elif i != 0 and j == 0:
                dp[i][j] = matrix[i][j] + matrix[i-1][j]
            else:
                dp[i][j] = matrix[i][j]+min(dp[i-1][j],dp[i][j-1])

    return (dp[-1][-1])
# matrix = []
# while True:
#     try:
#         line = list(map(int,input("请输入：").split()))
#         matrix.append(line)
#     except ValueError:
#         break
# print(getMintracefromMatrix(matrix))

'''
案例3：
给定数组arr，返回arr的最长递增子序列的长度，比如arr=
[2,www.walltu.com,5VirtualTea_party,3,6,4,8,9,7]，最长递增子序列为[www.walltu.com,3,4,8,9]返回其长度为5.
'''

def LongestSubarr(arr):
    dp = [0]*len(arr)
    dp[0] = 1
    for i in range(1,len(arr)):
        m = 0
        for j in range(i):  #这个for循环旨在找到i之前的子序列最大长度
            # if d p[j]>m and arr[i]>arr[j]:
                m = dp[j]
        dp[i] = m + 1   #位置i的最大子序列长度
    print(dp)
    return max(dp)  #返回dp数组的最大值
# arr = list(map(int,input("请输入数组：").split()))
# print(LongestSubarr(arr))

'''
案例四：
给定两个字符串str1和str2，返回两个字符串的最长公共子序列，
例如：str1="1A2C3D4B56",str2="B1D23CA45B6A","123456"和
"12C4B6"都是最长公共子序列，返回哪一个都行。
'''

'''
案例5：

背包问题，动态规划经典问题，一个背包有滴定的承重W，有N件物品，
每件物品都有自己的价值，记录在数组V中，也都有自己的重量，
记录在数组W中，每件物品只能选择要装入还是不装入背包，要求在
不超过背包承重的前提下，选出的物品总价值最大。
'''
def bag_problem(v,w,n,cap):
    num = []
    dp = [[0 for _ in range(cap+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,cap+1):
            if j >= w[i]:
                # dp[i][j] = max(dp[i-1][j-w[i]] + v[i],dp[i-1][j])
                #如何记录最佳方案？
                if dp[i-1][j-w[i]] + v[i] > dp[i-1][j]:
                    dp[i][j] = dp[i-1][j-w[i]] + v[i]
                    num.append(i)
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    print(num)
    print(dp[n][cap])

v = [0,4,5,6,10]     #这里数组添加0，可以将数组下标
w = [0,3,4,5,6]      #与物品件数对应起来，便于理解
n = 4
cap = 12
# bag_problem(v,w,n,cap)
'''
案例6：
钢条切割问题

输入：
价格数组：[0,1,5,8,9,10,17,17,20,24,30]
钢条长度：eg 7

输出：
最佳切割方案
最大收益
'''
def Cut_Rod(price_arr,length):
    best_r = [0 for _ in range(length+1)]
    best_l = [0 for _ in range(length+1)]   #保存某一长度钢条的最优切法的初始值
    for i in range(1,length+1):
        q = -1
        for j in range(1,i+1):
            tmp = price_arr[j] + best_r[i-j]
            # 不用max函数用if判断是便于保存最优切法
            if tmp > q:
                q = tmp
                best_l[i] = j
        best_r[i] = q
    # 最优切法
    n = length
    print("最优切法：",end='')
    while n > 0:
        print(best_l[n],end=' ')
        n -= best_l[n]
    print()

    print("最大收益：" ,best_r[length])
    return best_r[length]

# p = [0,1,7,8,9,10,17,17,20,24,30]
# l = 6
# Cut_Rod(p,l)
























