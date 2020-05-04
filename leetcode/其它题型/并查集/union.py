'''
并查集类
用来解决并查集问题，独立位一个类，便于重复利用
'''
class Union():

    def __init__(self,n):
        #初始化变量和变量值
        self.pre = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self,x) -> int:
        while self.pre[x] != x:
            #边查找边路径压缩
            self.pre[x] = self.pre[self.pre[x]]
            x = self.pre[x]
        return x

    def connected(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] >= self.size[root_y]:
                self.pre[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.pre[root_x] = root_y
                self.size[root_y] += self.size[root_x]

            self.count -= 1
        else:
            return

    def get_count(self) -> int:
        return self.count

