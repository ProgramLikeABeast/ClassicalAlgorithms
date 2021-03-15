from ClassicAlgorithms.GraphRepresentation import Graph
from ClassicAlgorithms.LinkedList import Queue


def spu(graph, start):
    queue = Queue()
    queue.push(start)
    mapping = {}
    for i in graph.dict:
        mapping[i] = float("inf")
    mapping[start] = 0
    graph.visited[start] = True
    while not queue.isEmpty():
        root = queue.pop()
        for node in graph.dict[root]:
            if not graph.visited[node]:
                queue.push(node)
                mapping[node] = mapping[root] + 1
                graph.visited[node] = True
    return mapping


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
    graph.disconnect('b', 'c')
    graph.showList()
    print(spu(graph, 's'))
    graph.showList()


if __name__ == '__main__':
    main()
