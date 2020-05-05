'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from leetcode.其它题型.并查集.union import *
from leetcode.time_vs import time_this_function
class Solution:

    @time_this_function
    #并查集
    def solve_1(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return []

        # for line in board:
        #     print(line)
        m,n = len(board),len(board[0])
        uf = Union(m*n)

        def is_side(i,j,m,n) -> bool:
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                return True
            return False
        def get_index(i,j) -> int:
            return i * n + j
        for i in range(m):
            for j in range(n):
                #从边界上的 'O'开始，连接周围的 'O'
                if board[i][j] == 'O' and is_side(i,j,m,n):
                    queue = [(i,j)]
                    while queue:
                        i,j = queue.pop(0)
                        for (x,y) in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                            if -1 < x < m and -1 < y < n:
                                if board[x][y] == 'O' and not uf.is_connected(get_index(i,j),get_index(x,y)):
                                    uf.connect(get_index(i,j),get_index(x,y))
                                    queue.append((x,y))
        #将内部的未连接的 'O'改为'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not is_side(i,j,m,n) and uf.find(get_index(i,j)) == get_index(i,j):
                    board[i][j] = 'X'

        return board

    @time_this_function
    #bfs
    def solve_2(self, board: [[str]]) -> None:
        if board == []:
            return []

        m,n = len(board),len(board[0])

        def is_side(i,j,m,n) -> bool:
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                return True
            return False
        #将边界的 'O'点入队
        queue = []
        for i in range(m):
            for j in range(n):
                if is_side(i,j,m,n) and board[i][j] == 'O':
                    queue.append((i,j))
                    board[i][j] ='#'
        #标记不可围绕区域
        while queue:
            i,j = queue.pop(0)
            for (x,y) in [(i,j-1),(i-1,j),(i,j+1),(i+1,j)]:
                if -1 < x < m and -1 < y < n and board[x][y] == 'O':
                    queue.append((x,y))
                    board[x][y] = '#'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    continue
        # print(board)
        return board


#测试
if __name__ == "__main__":
    board = [["X","O","O","X","X","X","O","X","X","O","O","O","O","O","O","O","O","O","O","O"],
             ["X","O","O","X","X","O","O","X","O","O","O","X","O","X","O","X","O","O","X","O"],
             ["O","O","O","X","X","X","X","O","X","O","X","X","O","O","O","O","X","O","X","O"],
             ["O","O","O","X","X","O","O","X","O","O","O","X","X","X","O","O","X","O","O","X"],
             ["O","O","O","O","O","O","O","X","X","X","O","O","O","O","O","O","O","O","O","O"],
             ["X","O","O","O","O","X","O","X","O","X","X","O","O","O","O","O","O","X","O","X"],
             ["O","O","O","X","O","O","O","X","O","X","O","X","O","X","O","X","O","X","O","X"],
             ["O","O","O","X","O","X","O","O","X","X","O","X","O","X","X","O","X","X","X","O"],
             ["O","O","O","O","X","O","O","X","X","O","O","O","O","X","O","O","O","X","O","X"],
             ["O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O","X","O"],
             ["X","O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O"],
             ["O","X","O","O","O","X","O","X","O","X","X","O","X","X","X","O","X","X","O","O"],
             ["X","X","O","X","O","O","O","O","X","O","O","O","O","O","O","X","O","O","O","X"],
             ["O","X","O","O","X","X","X","O","O","O","X","X","X","X","X","O","X","O","O","O"],
             ["O","O","X","X","X","O","O","O","X","X","O","O","O","X","O","X","O","O","O","O"],
             ["X","O","O","X","O","X","O","O","O","O","X","O","O","O","X","O","X","O","X","X"],
             ["X","O","X","O","O","O","O","O","O","X","O","O","O","X","O","X","O","O","O","O"],
             ["O","X","X","O","O","O","X","X","X","O","X","O","X","O","X","X","X","X","O","O"],
             ["O","X","O","O","O","O","X","X","O","O","X","O","X","O","O","X","O","O","X","X"],
             ["O","O","O","O","O","O","X","X","X","X","O","X","O","O","O","X","X","O","O","O"]]

    res2 = Solution().solve_2(board)
    res1 = Solution().solve_1(board)
    print(res1==res2)