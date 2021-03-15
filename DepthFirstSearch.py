from ClassicAlgorithms.GraphRepresentation import Graph
from ClassicAlgorithms.LinkedList import Stack


def dfs_recursive(graph, start):
    graph.visited[start] = True
    for node in graph.dict[start]:
        if not graph.visited[node]:
            dfs_recursive(graph, node)
    return


def dfs_loop_v1(graph, start):
    stack = Stack()
    stack.push(start)
    while not stack.isEmpty():
        temp = stack.peek()
        graph.visited[temp] = True
        allVisited = True
        for node in graph.dict[temp]:
            if not graph.visited[node]:
                stack.push(node)
                graph.visited[node] = True
                allVisited = False
                break
        if allVisited:
            stack.pop()


def dfs_loop_v2(graph, start):
    stack = Stack()
    stack.push(start)
    while not stack.isEmpty():
        temp = stack.pop()
        if not graph.visited[temp]:
            graph.visited[temp] = True
            for node in graph.dict[temp]:
                if not graph.visited[node]:
                    stack.push(node)


def main():
    connectionArray = [['a', 'b'], ['b', 'd'], ['b', 'c'], ['d', 'c'], ['d', 'f'],
                       ['c', 'e'], ['e', 'g'], ['e', 'h'], ['a', 'g']]
    graph = Graph(['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g'])
    graph.quickConnect(connectionArray)
    dfs_recursive(graph, 'a')
    graph.showList()
    print()
    connectionArray2 = [['a', 'b'], ['b', 'd'], ['b', 'c'], ['d', 'c'], ['d', 'f'],
                        ['c', 'e'], ['e', 'g'], ['e', 'h'], ['a', 'g']]
    graph2 = Graph(['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g'])
    graph2.quickConnect(connectionArray2)
    dfs_loop_v2(graph2, 'a')
    graph2.showList()


if __name__ == '__main__':
    main()
