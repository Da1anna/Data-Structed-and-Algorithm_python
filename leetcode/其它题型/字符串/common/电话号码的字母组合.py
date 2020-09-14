# -*- coding:utf-8 -*-
# @Time: 2020/6/20 15:59
# @Author: Lj
# @File: 电话号码的字母组合.py

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    def letterCombinations(self, digits: str) -> [str]:
        """暴力递归"""
        d = {'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r','s'],
             '8':['t','u','v'],
             '9':['w','x','y','z']}
        res = []
        if not digits:
            return res

        def helper(i, str):
            if i == len(digits):
                res.append(str)
                return

            for a in d[digits[i]]:
                helper(i+1, str + a)

        helper(0,'')
        return res

#测试
digits = '234'
res = Solution().letterCombinations(digits)
print(res)