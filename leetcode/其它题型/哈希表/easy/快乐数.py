'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
正解思路：快慢指针破环
            为啥一定不会出现死循环，因为int类型最大值为为‭‭2 147 483 647‬‬， 
            所以平方和最大的数是1 999 999 999，平方和为1 + 81*9 = 724。
            任何数的平方和都在1到724之间，724次循环之内一定有重复
            
            快慢指针为啥能破除重复呢，这可以想象两个跑步的人在操场跑步，跑得快的人一定会
            和慢的相遇，操场可以看作1-724之间的数组成的跑道
'''
class Solution:

    #递归版，DIY,时空效果都很差
    def isHappy(self, n: int) -> bool:
        #特判
        if n == 0:
            return False

        def depart(n) -> list:
            nums = []
            while n:
                nums.append(n%10)
                n = n//10
            return nums

        def helper(nums: list) -> bool:
            nonlocal time
            squ_sum = 0
            for a in nums:
                if a not in d:
                    d[a] = a*a
                squ_sum += d[a]
            #边界条件
            if squ_sum == 1:
                return True
            time += 1
            if time == 100:
                return False
            return helper(depart(squ_sum))
        #哈希表记录数的平方和
        d = {}
        time = 0    #记录递归的次数
        return helper(depart(n))
    #循环版
    def isHappy_1(self, n: int) -> bool:
        if n == 0:
            return False
        def depart(n) -> list:
            nums = []
            while n:
                nums.append(n%10)
                n = n//10
            return nums

        d = {}
        squ_sum = n
        time = 0
        while squ_sum != 1 and time < 100:
            nums = depart(squ_sum)
            squ_sum = 0
            for a in nums:
                if a not in d:
                    d[a] = a*a
                squ_sum += d[a]
            time += 1

        if squ_sum == 1:
            return True
        return False

    #参考答案：快慢指针法
    def isHappy_2(self, n: int) -> bool:
        def get_squSum(n):
            squ_sum = 0
            while n:
                a = n%10
                squ_sum += a*a
                n = n//10
            return squ_sum

        #快慢指针法
        p = n
        q = get_squSum(n)
        while p != q:
            p = get_squSum(p)
            q = get_squSum(get_squSum(q))
        return p == 1


#测试
n = 19
res = Solution().isHappy_2(n)
print(res)

