# -*- coding:utf-8 -*-
# @Time: 2020/9/11 10:15
# @Author: Lj
# @File: reverse_str.py

def reverse_str(s:str)-> str:
    lst_s = s.split()
    r_lst_s = lst_s[-1::-1]
    r_s = ' '.join(r_lst_s)
    return r_s


s = "lao gan die"
res = reverse_str(s)
print(res)