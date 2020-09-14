# -*- coding:utf-8 -*-
# @Time: 2020/9/5 16:37
# @Author: Lj
# @File: 热土豆问题.py

'''
一群小孩围坐成一个圈，从某一个小孩开始，沿顺时针方向传递土豆，在固定时间内，
每次淘汰一个小孩，直到只剩一个小孩。
'''
def hotPotato(namelist, num):
    queue = namelist
    while len(queue) > 1:
        for i in range(num):
            queue.insert(0, queue.pop())
        out = queue.pop()
        # print(out)
    return queue[0]


namelist = ['赵', '钱', '孙', '李', '周', '吴', '郑', '刘']
res = hotPotato(namelist, 5)
print(res)

