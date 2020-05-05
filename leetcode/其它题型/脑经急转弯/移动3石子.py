'''
三枚石子放置在数轴上，位置分别为 a，b，c。

每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]

 

示例 1：

输入：a = 1, b = 2, c = 5
输出：[1, 2]
解释：将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。
示例 2：

输入：a = 4, b = 3, c = 2
输出：[0, 0]
解释：我们无法进行任何移动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/moving-stones-until-consecutive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> [int]:
        x, y, z = sorted([a, b, c])
        #三个数相邻时
        if y - x == 1 and z - y == 1:
            min_move = 0
        #移动的最小值为1时，有两种情况：1>两个数相邻，2>两个数相间，这时可将另一个数一步移动其中间
        elif y - x <= 2 or z - y <= 2:
            min_move = 1
        else:
            min_move = 2
        #最大移动步数计算都是一样，计算三个数的间隔即可
        max_move = (y - x - 1) + (z - y - 1)
        return [min_move,max_move]

#测试
res = Solution().numMovesStones(1,3,5)
print(res)