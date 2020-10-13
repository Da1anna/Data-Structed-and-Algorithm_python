# -*- coding:utf-8 -*-
# @Time: 2020/10/8 16:04
# @Author: Lj
# @File: 去除重复字母.py

'''
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：用栈控制进入与弹出元素
    不容易想到
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #用字典记录出现的字母及其次数
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        #栈维护的的是字典序最小的去重的字符组合
        stack = []
        for c in s:
            count[c] -= 1   #遍历到的字母次数减一
            #如果字母在栈中，则跳过，遍历下一个字母
            if c in stack:
                continue
            #如果不在，则要分情况讨论
            while stack and stack[-1] > c:
                if count[stack[-1]] == 0:
                    break

                else:
                    stack.pop()
            stack.append(c)
        res = ''.join(stack)
        return res

#测试
s = 'cbacdcbc'
res = Solution().removeDuplicateLetters(s)
print(res)


