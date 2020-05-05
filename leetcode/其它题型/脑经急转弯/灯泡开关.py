'''
初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。

示例:

输入: 3
输出: 1
解释:
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭].

你应该返回 1，因为只有一个灯泡还亮着。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bulb-switcher
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from math import sqrt
class Solution:
    def bulbSwitch_1(self, n: int) -> int:
        '''
        思路：第n个灯泡的状态取决于n的公约数的个数（包括1和n）,奇数为开
              开着的灯泡的总数：n加上n-1个时的数
        '''
        #n = 1时，为1
        count = 1

        #从2开始计算
        for i in range(2,n+1):
            m = 2   #1和本身算因数
            for j in range(2,i):
                if i % j == 0:
                    m += 1
            #为奇数，灯泡开
            if m % 2 == 1:
                count += 1
        return count

    #方法一是对的，只是超时了，这里返回从方法一观察到的规律

    def bulbSwitch_2(self, n: int) -> int:
        return int(sqrt(n))
#测试
if __name__ == "__main__":
    for i in range(1,100):
        res = Solution().bulbSwitch_1(i)
        print(i,':',res)