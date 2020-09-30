''''''
'''
1.图ADT的邻接表实现
'''
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
       return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __contains__(self,key):
        return key in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())


#测试
g = Graph()
for i in range(4):
    g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,2,4)
g.addEdge(1,2,3)
g.addEdge(1,3,3)
g.addEdge(2,4,1)
g.addEdge(2,5,2)

# for v in g:
#     print(v)
# print(g.getVertex(1))

'''
2.图的遍历(非强连通图也可以)
    2.1 BFS
        时间复杂度：O(V+E)
'''

def BFS(g:Graph):
    queue = []
    visited = set()
    res = []

    def bfs(root):
        queue.append(root)
        visited.add(root)
        res.append(root.id)

        while queue:
            cur = queue.pop(0)
            for nbr in cur.getConnections():
                if nbr not in visited:
                    queue.append(nbr)
                    visited.add(nbr)
                    res.append(nbr.id)

    for node in g:
        if node not in visited:
            bfs(node)
    return res


'''
    2.2 DFS
    
'''
#递归版
def DFS(g:Graph):
    visited = set()
    res = []

    def dfs(node):
        res.append(node.id)
        visited.add(node)
        for nbr in node.getConnections():
            if nbr not in visited:
                dfs(nbr)
    for node in g:
        if node not in visited:
            dfs(node)
    return res

#非递归版:不是强连通图也可以
def DFS_NR(g:Graph):
    stack = []
    visited = set()
    res = []

    def dfs(root):
        stack.append(root)
        visited.add(root)
        res.append(root.id)

        while stack:
            cur = stack[-1]
            hasChild = False
            for nbr in cur.getConnections():
                if nbr not in visited:
                    stack.append(nbr)
                    visited.add(nbr)
                    res.append(nbr.id)
                    hasChild = True
                    break
            if not hasChild:
                stack.pop()

    for node in g:
        if node not in visited:
            dfs(node)
    return res

#测试
# res1 = DFS(g)
# res2 = DFS_NR(g)
# print(res1,res2,sep='\n')


'''
3.最短路径问题
    定义：在图中寻找加权最短路径
    
    思路：经典的算法是“Dijkstra”算法
        存储起点到某一个的整个路径的距离：(set)getDistance
        广度优先遍历 + 优先队列：优先队列保证每次从最小Distance点开始遍历
        在Vertex点上存储Pred前驱：用于打印最短路径
    理解：
        优先队列的目的是提升效率，每次优先队列弹出的是距起点最短距离的点，
        这样大概率能最快找到最短路径，当遍历其它路径的点时，因为其距离较大，
        不满足条件，便不继续下面的操作。  
    
'''
from pythonds import PriorityQueue, Graph, Vertex

def Dijkstra(graph,start):
    start.setDistance(0)
    pq = PriorityQueue()
    pq.buildHeap([(v.getDistance(), v) for v in graph])

    while not pq.isEmpty():
        curNode = pq.delMin()
        for nbr in curNode.getConnections():
            newDist = curNode.getDistance() + curNode.getWeight(nbr)
            if newDist < nbr.getDistance():
                nbr.setDistance(newDist)
                nbr.setPred(curNode)
                pq.decreaseKey(nbr, newDist)    #看源码理解这个方法

#测试通过

'''
4.最小生成树
    定义：在图中寻找一个包括指定节点的最小代价和的树
    应用：解决广播问题
        一个广播如何高效的将信息通过网络发送给它的听众
    思路：Prim算法
        和Dijkstra算法思路很相似，都是贪心的思路
        从起点开始，每次加入一个点，构成最小代价的树，直到加入所有点
        
'''
from pythonds import PriorityQueue, Graph, Vertex
def Prim(graph,start):
    start.setDistance(0)
    pq = PriorityQueue()
    pq.buildHeap([(v.getDistance(),v) for v in graph])

    while not pq.isEmpty():
        curNode = pq.delMin()
        for nbr in curNode.getConnections():
            newDist = curNode.getDistance() + curNode.getWeight(nbr)
            if nbr in pq and newDist < newDist.getDistance():
                nbr.setDistance(newDist)
                nbr.setPred(curNode)
                pq.decreaseKey(nbr, newDist)



'''
5.拓扑排序
    
'''



































