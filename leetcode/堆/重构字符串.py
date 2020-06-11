'''
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorganize-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路1：双指针交换法，遍历数组，当遇到一个字母与它之前一个不同时，从当前位置开始寻找一个可交换的字母，直到遍历完。
        这个思路对 ‘baaba’就不行了，因为它无法将第一个b交换到后面
        
思路2：将每一类字母及其个数组合成一个元组，加入堆中，每次弹出两个不同的个数最多的字母，更新其个数，
        重复直到弹完
        
'''

import heapq as hp
class Solution:

    #双指针交换
    def reorganizeString_demo(self, S: str) -> str:
        lst = list(S)

        for i in range(1, len(lst)):
            if lst[i] == lst[i - 1]:
                j = i+1
                while j < len(lst) and lst[j] == lst[i]:
                    j += 1
                if j < len(lst):
                    lst[i], lst[j] = lst[j], lst[i]
                else:
                    return ''
        return ''.join(lst)

    #堆的巧用：一次性弹出两个元素
    def reorganizeString(self, S: str) -> str:
        #特判
        if len(S) == 1:
            return S

        heap = [(-S.count(x),x) for x in set(S)]
        for cnt,x in heap:
            #这里的判断需要考虑len的奇偶
            if -cnt >= (len(S)+1)//2 + 1:
                return ''

        hp.heapify(heap)
        res = ''
        while len(heap) >= 2:
            cnt1, c1 = hp.heappop(heap)
            cnt2, c2 = hp.heappop(heap)
            res += c1 + c2
            if cnt1 + 1:
                hp.heappush(heap,(cnt1+1,c1))
            if cnt2 + 1:
                hp.heappush(heap,(cnt2+1,c2))

        return res+heap[0][1] if heap else res
#测试
S = 'aaab'
res = Solution().reorganizeString(S)
print(res)