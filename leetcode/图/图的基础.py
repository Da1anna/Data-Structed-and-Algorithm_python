'''
1.图的邻接表的实现
'''

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}       #字典的key：verTex,value:数字（weight）

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight      #字典的key可以是很多东西，不只是字符串

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])      #这种是在遍历字典的key


class Graph:

    def __init__(self):
        self.vertList = {}      #字典的key:字符串或数字(由输入决定)，value：Vertex
        # self.numVertex = 0

    def addVertex(self,key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


# g = Graph()
# for i in range(6):
#     g.addVertex(i)
# print(g.vertList)
# print(g.getVertices())
#
# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
# for v in g:
#     for w in v.getConnections():
#         print("( %s--%s : %s )" % (v.getId(), w.getId(), v.getWeight(w)))


'''
2.广度优先遍历BFS和深度优先遍历DFS
注:这里考虑的是强连通图
'''

#初始化图
# vertex_1= [1,2,3,4,5,6]
# edge_1 = [(1,2),(1,6),(2,3),(2,5),(3,4),(3,1),(4,1),(4,5),(5,3),(5,4)]
#
# vertex_2= [1,2,3,4,5]
# edge_2 = [(1,2),(1,3),(2,4),(2,5)]
# g = Graph()
# for v in vertex_2:
#     g.addVertex(v)
# for cur,edge in edge_2:
#     g.addEdge(cur,edge)
# for v in g:
#     for w in v.getConnections():
#          print("( %s--%s )" % (v.getId(), w.getId()))

#2.1 BFS
def BFS(g:Graph,start:Vertex):
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)

    while queue:
        cur = queue.pop(0)
        for nbr in cur.getConnections():
            if nbr not in visited:
                queue.append(nbr)
                visited.add(nbr)
        print(cur.id)

# BFS(g,g.getVertex(1))

#2.2 DFS
def DFS(g:Graph,start:Vertex):
    stack = []
    stack.append(start)
    visited = set()
    visited.add(start)

    res = [start.id]
    while stack:
        cur = stack[-1]
        found_newV = False      #记录是否找到cur的未访问过的邻节点
        # res.append(cur)
        for nbr in cur.getConnections():
            if nbr not in visited:
                #发现一个未被访问的节点的处理：
                visited.add(nbr)
                stack.append(nbr)
                res.append(nbr.id)
                found_newV = True
                break
            else:
                continue
        if  not found_newV:
            stack.pop()

    print(res)

# DFS(g,g.getVertex(1))


'''
3 最短路径——Dijkstra算法
'''
from pythonds import PriorityQueue,Graph,Vertex

def dijkstra(aGraph:Graph,start:Vertex):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])

    # while not pq.isEmpty():
    while pq.currentSize > 1:  # 保留优先队列一个值的原因是优先队列的初始化时会先加一个（0，0）元组，用处是便于计算堆的索引

        curV = pq.delMin()
        for nextV in curV.getConnections():
            newDist = curV.getDistance() + curV.getWeight(nextV)
            if newDist < nextV.getDistance():
                nextV.setDistance(newDist)
                nextV.setPred(curV)
                pq.decreaseKey(nextV,newDist)   #这个方法应该是内部调用了percUp(),有调整堆的味道

#初始化图
v = ['u','v','x','w','y','z']
#无向图一定要这样创建吗？
edge = [('u','v',2),('u','w',5),('u','x',1),
        ('v','u',2),('v','x',2),('v','w',3),
        ('x','u',1),('x','v',2),('x','w',3),('x','y',1),
        ('w','v',2),('w','u',5),('w','x',3),('w','y',1),('w','z',5),
        ('y','x',1),('y','w',1),('y','z',1),
        ('z','w',5),('z','y',1)]

g = Graph()
g.addVertex(v for v in v)
for cur,nbr,weight in edge:
    g.addEdge(cur, nbr, weight)
# print(g.getVertex('w'))

#测试
dijkstra(g,g.getVertex('u'))
for v in v[1:]:
    print('u到%s的最短距离：%i' % (v,g.getVertex(v).getDistance()))


'''
4.最小生成树
注：同Dijkstra算法很相似
'''

def Prim(aGraph:Graph,start:Vertex):
    pq = PriorityQueue()
    # for v in aGraph:
    #     v.setDistance(100)
    #     v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])

    res = []
    # while not pq.isEmpty():
    while pq.currentSize > 1:   #保留优先队列一个值的原因是优先队列的初始化时会先加一个（0，0）元组，用处是便于计算堆的索引
        curV = pq.delMin()
        for nbr in curV.getConnections():
            cost = curV.getWeight(nbr)
            if nbr in pq and cost < nbr.getDistance():
                nbr.setDistance(cost)
                nbr.setPred(curV)
                pq.decreaseKey(nbr,cost)
        res.append(curV.id)
    # res.pop()
    print(res)

#测试
# Prim(g,g.getVertex('u'))
#结果为何多了一个东西<generator object？？？


