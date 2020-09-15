'''
1.[分数背包问题]  可以用贪心求最优解
有一个背包，背包容量是M=150。有7个物品，物品可以分割成任意大小。
要求尽可能让装入背包中的物品总价值最大，但不能超过总容量。

物品 A  B  C  D  E  F  G

重量 35 30 60 50 40 10 25

价值 10 40 30 50 35 40 30
'''
class goods():
    def __init__(self,id,weight,value):
        self.id = id
        self.w = weight
        self.v = value
    def __str__(self):
        return str(self.id) + ' w:'+ str(self.w) + ' v:' + str(self.v)

def greedy_for_bag(cap:int,some_goods:list):
    #对物品列表按重量价值比由高到低排序
    some_goods.sort(key=lambda goods:- (goods.v/goods.w))

    # print('排序后：',end='')
    # for i in some_goods:
    #     print(i,end=' | ')
    res = []
    i = 0
    for item in some_goods:
        if cap < item.w:
            break
        res.append(item)
        i += 1
        cap -= item.w
    if len(res) != len(some_goods) and cap != 0:
        res.append(goods(some_goods[i].id,cap,cap/some_goods[i].w*some_goods[i].v))
    #输出结果
    # print()
    print('结果集：',end='')
    for i in res:
        print(i,end=' | ')
    return res

some_goods = [goods('A',35,10),goods('B',30,40),goods('C',60,30),goods('D',50,50)]
# greedy_for_bag(100,some_goods)

# a = goods('A',35,10)
# print(a)      #打印单个class:goods可以
# print(some_goods)     #不能打印一个装有goods的列表？？？？？


'''
2.[0-1背包问题]     用贪心不能求求最优解，可用动态规划求解
物品不可分割，其它同分数背包问题
'''



'''
3.[均分纸牌]
有N堆纸牌，编号分别为1，2，…，n。每堆上有若干张,但纸牌总数必为n的倍数.
可以在任一堆上取若干张纸牌,然后移动。
移牌的规则为：在编号为1上取的纸牌，只能移到编号为2的堆上；在编号为n的堆上取的纸牌，只能移到编号为n-1的堆上；
其他堆上取的纸牌，可以移到相邻左边或右边的堆上。现在要求找出一种移动方法，用最少的移动次数使每堆上纸牌数都一样多。
例如：n=4，4堆纸牌分别为：① 9 ② 8 ③ 17 ④ 6 
移动三次可以达到目的：从③取4张牌放到④ 再从③区3张放到②然后从②去1张放到①。

输入输出样例：4

9 8 17 6

输出：3

注：感觉跟贪心算法不算很有关系
'''
def junfen_cards(lst:list) -> int:
    k = sum(lst)//len(lst)
    n = 0
    for i in range(len(lst)-1):
        need = k - lst[i]
        if need != 0:
            lst[i] = k
            lst[i+1] = lst[i+1] - need
            n += 1
    return n

# res = junfen_cards([0,0,5,0,0])
# print(res)


'''
4.[找零钱问题]
假设只有 1 分、 2 分、5分、 1 角、二角、 五角、 1元的硬币
求1.84元最少找几个硬币？

注：这个零钱问题可以用贪心求解，因为零钱数额很 “标致”
'''

def find_change(lst:list,change):
    # n = 0     #只计算个数
    lst_n = [0 for _ in lst]    #列举找了哪些硬币
    while change != 0:
        if change >= lst[-1]:
            change  = round(change - lst[-1],2)     #限制数字的位数，因为浮点数计算不精确
            # n += 1
            lst_n[lst.index(lst[-1])] += 1
        else:
            lst.pop()
    return lst_n
lst= [0.01,0.02,0.05,0.1,0.2,0.5,1]
change = 1.85
# res = find_change(lst,change)
# print(res)
#

'''
5.[求最大子数组之和]
问题：给定一个整数数组（数组元素有负有正），求其连续子数组之和的最大值。
'''


'''
6.[汽车加油问题]
一辆汽车加满油后可行驶n公里。旅途中有若干个加油站。设计一个有效算法，
指出应在哪些加油站停靠加油，使沿途加油次数最少。 
对于给定的n(n <= 5000)和k(k <= 1000)个加油站位置，编程计算最少加油次数。
'''

'''
7.[救生艇]
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
每艘船最对容纳2个人
返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

示例 1：

输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
示例 2：

输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
示例 3：

输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)
提示：

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
'''
def jiushengting(people:list, limit:int) -> int:
    one_ship = []
    res = []
    i,j = 0,len(people) - 1
    people.sort()
    while i <= j:
        one_ship.append(people[j])      #people[j]怎么都是要装的
        if people[i] + people[j] <= limit:
            one_ship.append(people[i])
            i += 1
        j -= 1
        res.append(one_ship)
        one_ship = []       #没循环一次，一定走一艘船
    print(res)
    return len(res)

# print(jiushengting([5,1,2,4],6))