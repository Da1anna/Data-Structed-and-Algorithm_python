'''
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。

请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

你需要原地修改栈。

示例1:

 输入：A = [2, 1, 0], B = [], C = []
 输出：C = [2, 1, 0]
示例2:

 输入：A = [1, 0], B = [], C = []
 输出：C = [1, 0]
提示:

A中盘子的数目不大于14个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hanota-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
注：汉诺塔问题有不同的规则：
        1.一种是柱子之间有顺序，盘子从A到C必须经过B ———— 结论：步数 = 2的n次方 - 1
        2.一种没有顺序，A可以直接到C ———— 结论：步数 = 3的n次方 - 1
    这道题就没有固定顺序
思路：递归就是自顶向下，从n开始考虑，变成n-1的问题，n-1继续变成n-2问题，最后变成1的问题，即是边界条件
    n:把上面的n-1个盘移到辅助柱B（辅助柱不是固定的，现在是B），把n移到C，变成n-1子问题
    n-1:要想把n-1个盘移到B，就先把上面的n-2个盘移到辅助柱C，把第n-1个移到B，变成n-2子问题
    ...
    ...
    2：把1移动到辅助柱，2移动到目的柱
    1：把1移动到目的柱
'''
class Solution:

    #上面第二种规则的写法
    def hanota_2(self, A: [int], B: [int], C: [int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        count = 0
        n = len(A)
        def helper(n,A,B,C):
            nonlocal count
            if n == 1:
                C.append(A.pop())
                count += 1
                return
            helper(n-1,A,C,B)   #将A柱（n盘）上面的n-1个盘从A经过辅助柱C全部移到B
            C.append(A.pop())   #A柱上面的第n盘直接移动到到C
            count += 1
            helper(n-1,B,A,C)   #将B柱上面的n-1个盘从B经过辅助柱A全部移到C

        helper(n,A,B,C)
        print(A,B,C,'次数:',count)


    #第一种规则的写法
    def hanota_1(self, A: [int], B: [int], C: [int]) -> None:
        count = 0
        n = len(A)

        def helper(n, A, B, C):
            nonlocal count
            if n == 1:
                B.append(A.pop())
                count += 1
                C.append(B.pop())
                count += 1
                return
            helper(n-1, A, B, C)
            B.append(A.pop())
            count += 1
            helper(n-1, C, B, A)
            C.append(B.pop())
            count += 1
            helper(n-1, A, B, C)

        helper(n, A, B, C)
        print(A, B, C,'步数：',count)

#测试
A = [4,3,2,1]
B,C = [],[]
print(Solution().hanota_2(A,B,C))