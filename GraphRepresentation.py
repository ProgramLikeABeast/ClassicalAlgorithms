class Graph:
    def __init__(self, arrayOfVertices):
        self.dict = {}
        self.visited = {}
        self.initialArray = arrayOfVertices
        for vertex in arrayOfVertices:
            self.dict[vertex] = []
            self.visited[vertex] = False

    def reversed(self):
        rev = Graph(self.initialArray)
        for vertex in self.dict:
            for edge in self.dict[vertex]:
                rev.dict[edge].append(vertex)
        return rev

    def size(self):
        return len(self.dict)

    def addVertex(self, vertex):
        self.dict[vertex] = []
        self.visited[vertex] = False

    def deleteVertex(self, vertex):
        if vertex in self.dict:
            self.dict.pop(vertex, None)
            self.visited.pop(vertex, None)
        for other in self.dict:
            if vertex in self.dict[other]:
                self.dict[other].remove(vertex)

    def quickConnect(self, array):
        for i in array:
            self.connect(i[0], i[1])

    def directedQuickConnect(self, array):
        for i in array:
            self.directedConnect(i[0], i[1])

    def connect(self, vertex1, vertex2):
        if vertex1 in self.dict and vertex2 in self.dict:
            if vertex1 not in self.dict[vertex2]:
                self.dict[vertex2].append(vertex1)
            if vertex2 not in self.dict[vertex1]:
                self.dict[vertex1].append(vertex2)

    def disconnect(self, vertex1, vertex2):
        if vertex1 in self.dict and vertex2 in self.dict:
            self.dict[vertex1] = [i for i in self.dict[vertex1] if i != vertex2]
            self.dict[vertex2] = [i for i in self.dict[vertex2] if i != vertex1]

    def directedConnect(self, vertex1, vertex2):
        if vertex1 in self.dict and vertex2 in self.dict:
            if vertex2 not in self.dict[vertex1]:
                self.dict[vertex1].append(vertex2)

    def getAllConnections(self, vertex):
        return self.dict[vertex]

    def showList(self):
        for i in self.dict:
            print(i, end=':')
            print(self.visited[i], end=' ')
            print(self.dict[i])


class weighedGraph(Graph):
    def __init__(self, arrayOfVertices):
        super().__init__(arrayOfVertices)
        self.edge = {}
        for i in arrayOfVertices:
            self.edge[i] = {}

    def connect(self, vertex1, vertex2, distance):
        if vertex1 in self.dict and vertex2 in self.dict:
            if vertex1 not in self.dict[vertex2]:
                self.dict[vertex2].append(vertex1)
            if vertex2 not in self.dict[vertex1]:
                self.dict[vertex1].append(vertex2)
            if vertex1 not in self.edge[vertex2]:
                self.edge[vertex2][vertex1] = distance
            if vertex2 not in self.edge[vertex1]:
                self.edge[vertex1][vertex2] = distance


def main():
    graph = Graph(['s', 'a', 'b', 'c', 'd', 'e'])
    graph.connect('s', 'a')
    graph.connect('s', 'b')
    graph.connect('a', 'c')
    graph.connect('b', 'c')
    graph.connect('b', 'd')
    graph.connect('c', 'd')
    graph.connect('c', 'e')
    graph.connect('d', 'e')
    graph.showList()


if __name__ == '__main__':
    main()
