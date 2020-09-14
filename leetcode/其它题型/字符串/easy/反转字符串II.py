'''
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 
示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路1：将反转封装成一个函数，分成三种情况来调用该函数
'''
class Solution:

    #时间击败31% + 写法过于臃肿
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s,l,r):
            while l<r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        arr_s = list(s)
        for i in range(0,len(arr_s), 2*k):
            if len(arr_s)-i < k:
                l, r = i, len(arr_s)-1
                reverse(arr_s,l,r)
                return ''.join(arr_s)

            elif k <= len(arr_s)-i <= 2*k:
                l, r = i, i+k-1
                reverse(arr_s,l,r)
                return ''.join(arr_s)

            else:
                l, r = i, i + k - 1
                reverse(arr_s,l,r)


#测试
s = 'abcdefg'
res = Solution().reverseStr(s,8)
print(res)
