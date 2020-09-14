# -*- coding:utf-8 -*-
# @Time: 2020/6/23 16:27
# @Author: Lj
# @File: 回文子串.py

'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
参考答案思路：中心拓展
            1.可以知道一共有2*N-1个回文串的中心：字符或两个字符之间
            2.对每个中心同时向左向右拓展，判断其是否是回文串
'''
class Solution:

    #暴力法：列举出所有字符串组合，对每个组合判断其是否是回文串
    #时间复杂度——O（1/4 n3）超时
    def countSubstrings(self, s: str) -> int:

        def is_huiwen(str) -> bool:
            i, j = 0, len(str)-1
            while i < j:
                if str[i] == str[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        count = 0
        for i in range(len(s)):
            j = i+1
            while j <= len(s):
                if is_huiwen(s[i:j]):
                    count +=1
                j += 1
        return count

    #参考答案：中心拓展法
    def countSubstrings_1(self, s: str) -> int:
        N = len(s)
        cnt = 0
        #在计算中心点的左右两边位置需要细心推敲
        for center in range(2*N-1):
            left = center // 2
            right = left + center % 2
            while left >=0 and right < N and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        return cnt

#测试
s = 'aba'
res = Solution().countSubstrings_1(s)
print(res)