'''
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/last-stone-weight
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import heapq
# class Solution:
def lastStoneWeight(stones) -> int:
    k = len(stones)
    stones = [-stones[i] for i in range(k)]
    heapq.heapify(stones)
    while len(stones) > 1:
        top1 = heapq.heappop(stones)
        top2 = heapq.heappop(stones)
        heapq.heappush(stones,top1-top2)
    return  - stones[0]

# res = lastStoneWeight([3,5,7])
# print(res)

'''
2.跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def keepJump(lst:list) -> bool:
    if len(lst) == 1:
        return True
    k = 0
    for i in range(len(lst)):
        if i > k:
            return False
        k = max(k,i+lst[i])
        if k >= len(lst) - 1:
            return True
# res = keepJump([3,2,1,1,4])
# print(res)


'''
3.跳跃游戏2
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def jump(lst:list) -> int:
    step = 0
    end = 0     #表示起跳的最远距离，若遍历的i==end了，说明该起跳了
    max_position = 0
    for i in range(len(lst)-1):
        max_position = max(max_position,i + lst[i])
        if i == end:    #这里虽然step不应该在i=3这个位置+1，但是steps是相同的
            step += 1
            end = max_position
    return step
# res = jump([3,1,4,1,1,1,0])
# print(res)

'''
4.判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.
'''
def is_Subsequence(s:str,t:str) -> bool:
    '''
    朴素的双子针法
    :param s: 原字符串
    :param t: 子字符串
    :return:
    '''
    i,j = 0,0
    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(t)

# res = is_Subsequence('abcde','ace')
# print(res)

'''
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证返回结果的字典序????最小（要求不能打乱其他字符的相对位置）。

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"
'''
def str_quchong(s:str) -> str:
    '''
    注：自己写的没有考虑到什么是字典序，所以不是该题的解
    :param s:
    :return:
    '''
    lst_s = [c for c in s]
    single = []
    for c in lst_s:
        if c not in single:
            single.append(c)
        else:
            continue
    single.sort()
    res = ''.join(c for c in single)
    print(res)
    return res
# str_quchong('ddcabdca')













