import random
from ClassicAlgorithms.GraphRepresentation import Graph
from ClassicAlgorithms.LinkedList import Stack


def kosaraju(graph):
    # 1. get the reversed-edge version of graph
    graphRev = graph.reversed()

    # 2. DFS the reversed graph
    unvisitedList = [node for node in graphRev.dict]
    stack = Stack()
    mapping = []
    while unvisitedList:
        print("**********")
        start = random.choice(unvisitedList)
        unvisitedList.remove(start)
        stack.push(start)
        while not stack.isEmpty():
            temp = stack.peek()
            if not graphRev.visited[temp]:
                mapping.append(temp)
            graphRev.visited[temp] = True
            allVisited = True
            for node in graphRev.dict[temp]:
                if not graphRev.visited[node]:
                    print("map length="+str(len(mapping)))
                    stack.push(node)
                    allVisited = False
                    unvisitedList.remove(node)
                    break
            if allVisited:
                newItem = stack.pop()
                mapping.append(newItem)

    print(mapping)
    # 3. BFS the original graph with the vertices
    result = []
    for i in reversed(range(len(mapping))):
        start = mapping[i]
        if graph.visited[start]:
            continue
        stack = Stack()
        stack.push(start)
        component = []
        # DFS
        stack = Stack()
        stack.push(start)
        while not stack.isEmpty():
            temp = stack.pop()
            if not graph.visited[temp]:
                graph.visited[temp] = True
                component.append(temp)
                for node in graph.dict[temp]:
                    if not graph.visited[node]:
                        stack.push(node)
        result.append(len(component))
    return result


def found(mapping, value):
    for i in mapping:
        if mapping[i] == value:
            return True
    return False


connectionArray = [['a', 'c'], ['e', 'a'], ['c', 'e'], ['c', 'k'], ['e', 'g'],
                   ['e', 'i'], ['k', 'f'], ['k', 'h'], ['h', 'f'], ['f', 'j'],
                   ['g', 'i'], ['d', 'g'], ['i', 'd'], ['i', 'b'], ['b', 'd'],
                   ['b', 'j'], ['j', 'h'], ['i', 'h']]
graph1 = Graph(['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g', 'h', 'i', 'j', 'k'])
connectionArray2 = [['1', '3'], ['1', '2'], ['4', '1'], ['2', '4'], ['3', '4'],
                    ['3', '5'], ['4', '6'], ['5', '6'], ['1', '1']]
graph2 = Graph(['1', '2', '3', '4', '5', '6'])
connectionArray3 = [['0', '1'], ['3', '0'], ['2', '3'], ['1', '2'], ['2', '4'],
                    ['4', '5'], ['5', '6'], ['6', '4'], ['6', '7']]
graph3 = Graph(['0', '1', '2', '3', '4', '5', '6', '7'])
graph4 = Graph([str(i) for i in range(1, 875715)])
graph1.directedQuickConnect(connectionArray)
graph2.directedQuickConnect(connectionArray2)
graph3.directedQuickConnect(connectionArray3)


def getSizeList(array):
    result = sorted([len(i) for i in array], reverse=True)
    return result


def main():
    with open("assign5_input.txt") as f:
        content = f.readlines()
    for line in content:
        string = line.strip()
        inputArray = string.split(" ")
        graph4.directedConnect(inputArray[0], inputArray[1])
    print("********************")
    print(sorted(kosaraju(graph4)))


if __name__ == '__main__':
    main()
