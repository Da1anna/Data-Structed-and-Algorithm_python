'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，
判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

'''

class Solution:
    def isValid(self, s: str) -> bool:
        chars = [i for i in s]  #字符串转换为字符列表
        stack = []
        for char in chars:
            if char in ["(","[","{"]:
                stack.append(char)
            if char in [")","]","}"]:
                if len(stack) == 0:
                    return False
                else:
                    if isMacth(self,stack[-1],char):
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
def isMacth(self,a,b):
    return (a =="(" and b ==")" or a == "[" and b == "]" or a == "{" and b == "}")
