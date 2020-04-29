'''
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:

 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:

 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 输出 true
提示：

节点数量n在[0, 1e5]范围内。
节点编号大于等于 0 小于 n。
图中可能存在自环和平行边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/route-between-nodes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findWhetherExistsPath(self, n: int, graph: [[int]], start: int, target: int) -> bool:
        #实现邻接链表
        from collections import defaultdict
        dict = defaultdict(list)
        for path in graph:
            dict[path[0]].append(path[1])

        #BFS
        visited,queue = [start],[start]
        while queue:
            cur = queue.pop(0)
            if cur == target:
                return True
            for nbr in dict[cur]:
                if nbr not in visited:
                    queue.append(nbr)
                    visited.append(nbr)
        return False

    def findWhetherExistsPalth_1(self, n: int, graph: [[int]], start: int, target: int) -> bool:
        # 实现邻接链表
        from collections import defaultdict
        dict = defaultdict(list)
        for path in graph:
            dict[path[0]].append(path[1])
        #DFS
        visited,stack = [0]*n,[start]
        while stack:
            cur = stack[-1]
            if cur == target:
                return True
            found_newV = False
            for nbr in dict[cur]:
                if visited[nbr] == 0:
                    stack.append(nbr)
                    visited[nbr] = 1
                    found_newV = True
                    break
            if not found_newV:
                stack.pop()
        return False



#测试
graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
start = 0
target = 4

res = Solution().findWhetherExistsPath_1(5,graph,start,target)
print(res)