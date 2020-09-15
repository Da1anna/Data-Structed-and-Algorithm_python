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
2.图的遍历
    2.1 BFS
        时间复杂度：O(V+E)
'''

def BFS(g:Graph):
    root = g.getVertex(0)
    queue = [root]
    visited = set()
    res = ''

    while queue:
        curVert = queue.pop(0)
        res += str(curVert.id)
        for nbr in curVert.getConnections():
            if nbr not in visited:
                queue.append(nbr)
                visited.add(nbr)
    return res

'''
    2.2 DFS
    
'''
#递归版
def DFS(g:Graph):

    def _helper(v,path,visited):
        path += str(v.id)
        visited.add(v)
        for nbr in v.getConnections():
            if nbr not in visited:
                path = _helper(nbr,path,visited)
        return path

    root = g.getVertex(0)
    path = ''
    visited = set()
    res = _helper(root,path,visited)
    return res

#非递归版





#测试
res1 = DFS(g)
res2 = BFS(g)
print(res1,res2,sep='\n')













