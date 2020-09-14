'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    def reverseWords(self, s: str) -> str:
        #反转单个单词的函数
        def reverse(s: str) -> str:
            arr_s = list(s)
            l, r = 0, len(arr_s)-1
            while l < r:
                arr_s[l], arr_s[r] = arr_s[r], arr_s[l]
                l += 1
                r -= 1
            return ''.join(arr_s)

        arr_s = s.split(' ')
        res = ''
        for word in arr_s:
            res += reverse(word) + ' '
        return res.strip()

    #相当简洁版
    #时间复杂度是是上面的一半，求解？
    def reverseWords_1(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split()])

#测试
s = "Let's take LeetCode contest"
res = Solution().reverseWords_1(s)
print(res)