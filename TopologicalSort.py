from ClassicAlgorithms.GraphRepresentation import Graph
from ClassicAlgorithms.LinkedList import Stack
import random


def ts(graph):
    unvisitedList = [node for node in graph.dict]
    stack = Stack()
    result = []
    while unvisitedList:
        start = random.choice(unvisitedList)
        unvisitedList.remove(start)
        stack.push(start)
        while not stack.isEmpty():
            temp = stack.peek()
            graph.visited[temp] = True
            allVisited = True
            for node in graph.dict[temp]:
                if not graph.visited[node]:
                    stack.push(node)
                    allVisited = False
                    unvisitedList.remove(node)
                    break
            if allVisited:
                newItem = stack.pop()
                result.insert(0, newItem)
    return result


def main():
    connectionArray = [['c', 'a'], ['e', 'a'], ['c', 'b'], ['b', 'd'], ['e', 'd'],
                       ['e', 'f'], ['d', 'h'], ['d', 'g'], ['g', 'i'], ['h', 'i'],
                       ['f', 'k'], ['k', 'j'], ['h', 'j'], ['i', 'l'], ['j', 'l'],
                       ['j', 'm'], ['a', 'd']]
    graph = Graph(['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
    graph.directedQuickConnect(connectionArray)
    graph.showList()
    print()
    print(ts(graph))
    print()
    graph.showList()


if __name__ == '__main__':
    main()
