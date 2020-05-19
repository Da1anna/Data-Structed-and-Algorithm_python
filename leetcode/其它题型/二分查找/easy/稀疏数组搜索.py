'''
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sparse-array-search-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：在二分查找的框架上处理一个特殊情况即可
但有一个用例过不了，没搞懂为啥
'''
class Solution:

    def findString(self, words: [str], s: str) -> int:

        l,h = 0,len(words)-1
        s = s.lower()
        while (l <= h):
            mid = (l + h)//2
            tmp = mid
            #遇到空字符串，则横向移动，找到一个非空字符串
            while words[mid] == '' and mid < h:
                mid += 1
            #跳出循环有下面两种情况
            #第一种
            if words[mid] == '':
                h = tmp-1
                continue
            #第二种就是找到一个非空值，这样就可以继续二分查找了
            if s == words[mid].lower():
                return mid
            elif s < words[mid].lower():
                h = mid -1
            elif s > words[mid].lower():
                l = mid + 1
        return -1

#测试
words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]
res = Solution().findString(words,"car")
print(res)