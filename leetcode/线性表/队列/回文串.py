# -*- coding:utf-8 -*-
# @Time: 2020/9/5 17:40
# @Author: Lj
# @File: 回文串.py
'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    #用双端队列
    def isPalindrome_1(self, s:str):
        deque = []
        for c in s:
            if c.isalnum():
                deque.append(c.lower())
        # print(deque)
        isEqual = True
        while len(deque) > 1 and isEqual:
            if deque.pop(0) != deque.pop():
                isEqual = False
        return isEqual

    #双指针
    def isPalindrome_2(self, s:str):
        plain_s = ''
        for c in s:
            if c.isalnum():
                plain_s += c
        plain_s = plain_s.lower()
        print(plain_s)
        l, r = 0, len(plain_s)-1
        isEqual = True
        while l < r:
            if plain_s[l] != plain_s[r]:
                isEqual = False
                break
            l += 1
            r -= 1
        return isEqual



s = "A man, a plan, a canal: Panama"
res = Solution().isPalindrome_2(s)
print(res)














