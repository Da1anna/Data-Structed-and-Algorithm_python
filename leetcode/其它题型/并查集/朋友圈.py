'''
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1:

输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
示例 2:

输入:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/friend-circles
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from leetcode.其它题型.并查集.union import *
from leetcode.time_vs import *

class Solution:
    @time_this_function

    def findCircleNum(self, M: [[int]]) -> int:
        '''
        方法一：广度优先遍历
             遍历每个人，找出这个人所有的朋友，入队
             对队列的每个人再找出所有其所有朋友，队空则完成一个朋友圈
             建立visited记录遍历过的人，遍历完所有人则结束
        :param M: 二维数组
        :return: 朋友圈个数
        '''
        def bfs(M) -> int:
            count = 0
            n = len(M)
            visited = []

            for i in range(n):
                if i in visited:
                    continue
                visited.append(i)
                queue = [i]
                while queue:
                    f = queue.pop(0)
                    for i in range(n):
                        if i not in visited and M[f][i] == 1:
                            queue.append(i)
                            visited.append(i)
                count +=1
            return count

        '''
        方法二：内部定义并查集
        '''
        def union(M) -> int:
            n = len(M)
            pre = [i for i in range(n)]
            count = n
            def find(x):
                p = pre[x]
                while p != x:
                    x = p
                    p = pre[p]
                return p
            def connected(x,y):
                nonlocal count      #处理全局变量和局部变量的一个技巧
                p_x = find(x)
                p_y = find(y)
                if p_x == p_y:
                    return
                pre[p_y] = p_x
                count -= 1
            def get_count():
                return count
            #初始化并查集
            for i in range(n):
                for j in range(i+1,n):
                    if M[i][j] == 1:
                        connected(i,j)
            #返回连接数
            return get_count()

        #方法三：引用优化和完整的并查集类
        n = len(M)
        uf = Union(n)
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j] == 1:
                    uf.connected(i,j)

        # return uf.get_count()
        return bfs(M)
        # return union(M)



#测试
if __name__ == "__main__":
    M = [
            [1,1,0],
            [1,1,0],
            [0,0,1]
    ]
    res = Solution().findCircleNum(M)
    print(res)








