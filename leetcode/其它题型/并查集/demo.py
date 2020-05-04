from copy import deepcopy
grid = [
    [1,1,1,0],
    [1,1,0,0],
    [1,0,0,1],
    [0,0,0,0]
]
# pre = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1 ]
pre = deepcopy(grid)
# pre[1][1] = 2
m,n = len(grid),len(grid[0])
# print(grid,pre)
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            pre[i][j] = (i, j)
# print(pre)
queue = [(1,5)]
cur = queue.pop(0)
print(cur[2])
