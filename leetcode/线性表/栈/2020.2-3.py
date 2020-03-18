
'''
一、栈
'''
'''

1.字符串解码

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

'''
# def solution(s:str):
#     stack,multi,res = [],0,""
#     for c in s:
#         if '0' <= c <= '9':
#             multi = multi * 10 + int(c)
#         elif c == '[':
#             stack.append([multi,res])
#             multi,res =0, ''
#         elif c == ']':
#             cur_multi,last_res = stack.pop()
#             res =last_res + cur_multi * res
#         else:
#             res += c
#     return res
# # s = input()
# s = '3[a20[c]]'
# print(solution(s))

'''
2.括号的分数
给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 

示例 1：

输入： "()"
输出： 1
示例 2：

输入： "(())"
输出： 2
示例 3：

输入： "()()"
输出： 2
示例 4：

输入： "(()(()))"
输出： 6
 

提示：

S 是平衡括号字符串，且只含有 ( 和 ) 。
2 <= S.length <= 50

'''
# def solution(s:str):
#     stack = []
#     for c in s:
#         if c == '(':
#             stack.append('(')
#         else:
#             if stack[-1] == '(':
#                 stack.pop()
#                 stack.append(1)
#             else:
#                 temp = stack.pop()
#                 while stack[-1] != '(':
#                     temp += stack.pop()     #temp储存A+B模式的AB和
#                 stack.pop()
#                 stack.append(2 * temp)      #append（A）模式的2A
#     return sum(stack)   #栈里可能会出现多个值，不能用pop(),要对数组求和
# s = '()()'
# print(solution(s))













