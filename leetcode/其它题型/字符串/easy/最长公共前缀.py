# -*- coding:utf-8 -*-
# @Time: 2020/6/19 15:49
# @Author: Lj
# @File: 最长公共前缀.py


class Solution:

    #时空很糟糕
    def longestCommonPrefix_1(self, strs: [str]) -> str:
        """自己的暴力思路"""
        #特判
        if not strs:
            return ''

        pre = strs[0]
        for i in range(len(pre)):
            for word in strs:
                if i < len(word) and word[i] == pre[i]:
                    continue
                else:
                    return pre[:i]
        return pre

    #先按字典序排序，再比较最大和最小值
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ''
        s1 = min(strs)
        s2 = max(strs)
        for i in range(len(s1)):
            if i < len(s2) and s1[i] == s2[i]:
                continue
            else:
                return s1[:i]
        return s1
#测试
strs = ['']
res = Solution().longestCommonPrefix(strs)
print(res)

