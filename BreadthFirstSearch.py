from ClassicAlgorithms.GraphRepresentation import Graph
from ClassicAlgorithms.LinkedList import Queue


def bfs(graph, start):
    queue = Queue()
    queue.push(start)
    for i in graph.visited:
        graph.visited[i] = False
    graph.visited[start] = True
    connectedComponents = [start]
    while not queue.isEmpty():
        root = queue.pop()
        for node in graph.dict[root]:
            if not graph.visited[node]:
                queue.push(node)
                graph.visited[node] = True
                connectedComponents.append(node)
    return connectedComponents


def unionFind(graph, node1, node2):
    for i in graph.visited:
        graph.visited[i] = False
    return node2 in bfs(graph, node1)


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
    graph.disconnect('c', 'e')
    graph.disconnect('d', 'e')
    print(bfs(graph, 's'))
    print(unionFind(graph, 's', 'e'))


if __name__ == '__main__':
    main()
