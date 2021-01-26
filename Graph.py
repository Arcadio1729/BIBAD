class Graph:
    GraphDict = {}  # to są pola klasowe - po co?
    VisitedDFS = None
    VisitedBFS = None
    QueueBFS = None

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.GraphDict = graph_dict # raczej snake_case
        self.VisitedDFS = []
        self.VisitedBFS = []
        self.QueueBFS = []

    def addVertex(self, v):
        if v not in self.GraphDict:
            self.GraphDict[v]=[]

    def addEdge(self, e):
        e = set(e)
        v1 = e.pop()
        if e:
            v2 = e.pop()
        else:
            v2 = v1

        """(v1, v2) = tuple(e)"""

        if v1 in self.GraphDict and v2 in self.GraphDict:
            self.GraphDict[v1].append(v2)
            self.GraphDict[v2].append(v1)



    def removeEdge(self, e):
        e = set(e)
        v1 = e.pop()
        if e:
            v2 = e.pop()
        else:
            v2 = v1

        if v1 in self.GraphDict:
            if self.GraphDict[v1].index(v2) > 0 and self.GraphDict[v2].index(v1) > 0:
                self.GraphDict[v1].remove(v2)

    def removeVertex(self, v):
        if v in self.GraphDict:
            self.GraphDict.pop(v)


    def getNeighbours(self, v):
        neighbours = []
        for n in self.GraphDict[v]:
            neighbours.append(n)

        return  neighbours

    def getVertices(self):
        return list(self.GraphDict.keys())

    def getEdges(self):
        edges = []
        for v in self.GraphDict:
            for n in self.GraphDict[v]:
                if {n, v} not in edges:
                    edges.append(v, n)

        return edges

    def DFS(self, v):   # z tej metody nic nie wynika - mogę uruchomić, ale nie pozwala mi przeiterować po wierzchołkach, żeby np. je wypisać
        if v not in self.VisitedDFS:
            self.VisitedDFS.append(v)
            for n in self.GraphDict[v]:
                self.DFS(n)

    def BFS(self, v):
        self.VisitedBFS.append(v)
        self.QueueBFS.append(v)

        while self.QueueBFS:
            temp = self.QueueBFS.pop(0)
            for n in self.GraphDict[temp]:
                if n not in self.VisitedBFS:
                    self.VisitedBFS.append(n)
                    self.QueueBFS.append(n)

if __name__ == "__main__":
    g = Graph()
    g.addVertex("a")
    g.addVertex("b")
    g.addVertex("c")
    g.addVertex("d")

    g.addEdge(('a', 'd'))
    g.addEdge(('a', 'c'))
    g.addEdge(('b', 'c'))
    g.addEdge(('a', 'b'))
    g.addEdge(('c', 'd'))

    g.DFS("a")
    g.BFS("a")
    print(g.GraphDict)
    print(g.VisitedDFS)
    print(g.VisitedBFS)

