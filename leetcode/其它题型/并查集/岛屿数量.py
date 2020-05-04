'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from leetcode.time_vs import time_this_function
from copy import deepcopy

class Solution:
    @time_this_function
    def numIslands_1(self, grid: [[str]]) -> int:
        '''
        方法一：并查集
        '''
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        #并查集类
        # 并查集类
        class Union():

            def __init__(self, grid):
                # 初始化变量和变量值
                self.pre = deepcopy(grid)
                self.size = deepcopy(grid)
                self.count = 0

            def instantiated(self, grid, m, n):
                for i in range(m):
                    for j in range(n):
                        if grid[i][j] == 1:
                            self.pre[i][j] = (i, j)
                            self.count += 1
                            self.size[i][j] = 1

            def find(self, x, y) -> ():
                while self.pre[x][y] != (x, y):
                    # 边查找边路径压缩
                    x_pre, y_pre = self.pre[x][y]
                    self.pre[x][y] = self.pre[x_pre][y_pre]
                    (x, y) = self.pre[x][y]
                return (x, y)

            def connect(self, x1, y1, x2, y2):
                (root_x1, root_y1) = self.find(x1, y1)
                (root_x2, root_y2) = self.find(x2, y2)
                if root_x1 != root_x2 or root_y1 != root_y2:
                    if self.size[root_x1][root_y1] >= self.size[root_x2][root_y2]:
                        self.pre[root_x1][root_y1] = self.pre[root_x2][root_y2]
                        self.count -= 1

                    else:
                        self.pre[root_x2][root_y2] = self.pre[root_x1][root_y1]
                        self.count -= 1
                else:
                    return

            def get_count(self) -> int:
                return self.count

        #初始化uf
        uf = Union(grid)
        uf.instantiated(grid,m,n)
        #连接岛屿
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for (x,y) in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                        if x > -1 and x < m and y > -1 and y < n and grid[x][y] == 1:
                            uf.connect(i,j,x,y)
        #返回岛屿数
        return uf.get_count()

    @time_this_function
    def numIslands_2(self, grid: [[str]]) -> int:
        '''
        BFS
        '''
        if grid == []:
            return 0
        m,n = len(grid),len(grid[0])
        visited = []
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    queue = [(i,j)]
                    visited.append((i,j))
                    while queue:
                        i,j = queue.pop(0)
                        for (x,y) in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                            if -1 < x < m and  -1 < y < n:
                                if grid[x][y] == 1 and (x,y) not in visited:
                                    queue.append((x,y))
                                    visited.append((x,y))
                    count += 1
        return count

    @time_this_function
    def numIslands_3(self, grid: [[str]]) -> int:
        '''
        DFS
        '''
        def dfs(x,y,visited,grid,m,n):
                visited[x][y] = True
                for (i,j) in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
                    if -1 < i < m and -1 < j < n:
                        if grid[i][j] == 1 and not visited[i][j]:
                            dfs(i,j,visited,grid,m,n)

        if grid == []:
            return 0
        m,n = len(grid),len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    dfs(i,j,visited,grid,m,n)
        return count
'''
'''

#测试
if __name__ == "__main__":
    grid = [
        [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    ]
    res1 = Solution().numIslands_1(grid)
    res2 = Solution().numIslands_2(grid)
    res3 = Solution().numIslands_3(grid)
    print(res1,res2,res3)