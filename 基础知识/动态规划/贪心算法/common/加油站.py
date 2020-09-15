# -*- coding:utf-8 -*-
# @Time: 2020/7/6 11:45
# @Author: Lj
# @File: 加油站.py

"""
134. 加油站
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明:

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
示例 1:

输入:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

输出: 3

"""

"""
思路：贪心策略：每次尝试剩余油量最多的一个加油站，看从其开始是否能够返回起点
        时间效率不好
"""
class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        #对每个加油站的剩余油量排序
        d = {}
        for i in range(len(gas)):
            d[i] = gas[i] - cost[i]
        d_list = sorted(d.items(),key=lambda item:item[1],reverse=True)

        #每次尝试油最多的加油站
        for cur_i, cur_left in d_list:
            #早停,没啥效果？
            if cur_left < 0:
                return -1
            #主体
            next_i = cur_i + 1 if cur_i+1 < len(gas) else 0
            total_left = cur_left
            while total_left >= 0 and next_i != cur_i:
                total_left += d[next_i]
                next_i = next_i+1 if next_i+1 < len(gas) else 0
            if total_left >=0 and next_i == cur_i:
                return cur_i
        return -1

#测试
gas  = [2,3,4]
cost = [3,4,3]

res = Solution().canCompleteCircuit(gas,cost)
print(res)