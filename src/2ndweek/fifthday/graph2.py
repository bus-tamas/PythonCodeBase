class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set()
    def addEdge(self, v1,v2):
        self.addVertex(v1)
        self.addVertex(v2)
        self.graph[v1].add(v2)
    def getVertex(self):
        return list(self.graph.keys())
    def getEdges(self):
        res = []
        for i in self.graph.keys():
            for j in self.graph[i]:
                res.append([i,j])
            return res
    def dfs(self):
        visited = set()
        for i in self.graph.keys():
            if i not in visited:
                self.callDFS(i,visited)
    
    def callDFS(self,src,visited):
        stack = []
        stack.append(src)
        visited.add(src)
        while len(stack):
            top = stack.pop()
            print(top, end = " ")
            for i in self.graph[top]:
                if i in self.graph[top]:
                    if i not in visited:
                        stack.append(i)
                        visited.add(i)
    def bfs(self):
        visited = set()
        for i in self.graph.keys():
            if i not in visited:
                self.callBFS(i,visited)
    
    def callBFS(self,src,visited):
        queue = []
        queue.append(src)
        visited.add(src)
        while len(queue):
            size = len(queue)
            for i in range(size):
                front = queue.pop(0)
                print(front,end = " ")
                for j in self.graph[front]:
                    if j not in visited:
                        queue.append(j)
            print()


g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'D')
g.addEdge('D', 'E')

print("DFS")
g.dfs()

print(g.getEdges())