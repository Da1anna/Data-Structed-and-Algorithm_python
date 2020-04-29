'''
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

 

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict

class Solution:
    '''
    方法一
    dfs遍历，若有环，则返回 false
    '''
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        #初始化邻接表
        dict = defaultdict(list)
        for pair in prerequisites:
            dict[pair[0]].append(pair[1])
        '''
        #DFS,若出现环，则不能
        #注意，这里的dfs不能用stack来写，原因自己分析
        visited,stack = [0],[0]
        while stack:
            cur_id = stack[-1]
            found_newV = False
            for nbr_id in dict[cur_id]:
                if nbr_id not in visited:
                    stack.append(nbr_id)
                    visited.append(nbr_id)
                    found_newV = True
                    break
            if not found_newV:
                stack.pop()
        '''

        #DFS
        flags = [0] * numCourses
        def dfs(cur_id,flags):
            if flags[cur_id] == -1:
                return True
            if flags[cur_id] == 1:
                return False
            flags[cur_id] = 1
            for nbr_id in dict[cur_id]:
                if not dfs(nbr_id,flags):
                    return False
            flags[cur_id] = -1
            return True
        for i in range(numCourses):
            if not dfs(i,flags):
                return False
        return True

    '''
    方法二
    拓扑排序，建立入度表，若能形成拓扑排序，则说明可行
    '''
    def canFinish_2(self, numCourses: int, prerequisites: [[int]]) -> bool:
        #建立入都表和临边
        in_degrees = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        for end,start in prerequisites:
            in_degrees[end] += 1
            adj[start].add(end)
        #拓扑排序
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        tuopu = []
        while queue:
            cur = queue.pop(0)
            tuopu.append(cur)
            for nbr in adj[cur]:
                in_degrees[nbr] -= 1
                if in_degrees[nbr] == 0:
                    queue.append(nbr)
        print(tuopu)
        return len(tuopu) == numCourses

#测试
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
res = Solution().canFinish_2(4,prerequisites)
print(res)