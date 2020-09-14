# -*- coding:utf-8 -*-
# @Time: 2020/9/5 10:44
# @Author: Lj
# @File: python_list_time.py

'''
测试python四种生成列表方式的时间
'''

#列表串联
def text1():
    l = []
    for i in range(1000):
        l = l + [i]

def text2():
    l = []
    for i in range(1000):
        l.append(i)

#列表推导
def text3():
    l = [i for i in range(1000)]

def text4():
    l = list(range(1000))

import timeit

print(timeit.timeit('text1()', setup='from __main__ import text1', number=1000))
print(timeit.timeit('text2()', setup='from __main__ import text2', number=1000))
print(timeit.timeit('text3()', setup='from __main__ import text3', number=1000))
print(timeit.timeit('text4()', setup='from __main__ import text4', number=1000))