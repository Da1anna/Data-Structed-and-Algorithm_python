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

    def addEdge(self,f,t,cost):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
print(g.getVertices())

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    for w in v.getConnections():
        print("( %s--%s : %s )" % (v.getId(), w.getId(), v.getWeight(w)))
