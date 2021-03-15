import random


def heapSort(array, reverse=False):
    result = []
    count = len(array)
    if reverse:
        heap = construct(array, "Max")
        while count > 0:
            result.append(maxHeapPop(heap))
            count -= 1
    else:
        heap = construct(array, "Min")
        while count > 0:
            result.append(minHeapPop(heap))
            count -= 1
    return result


def construct(array, policy):
    if policy == "Max":
        maxHeap = []
        for i in array:
            maxHeapInsert(maxHeap, i)
        return maxHeap
    elif policy == "Min":
        minHeap = []
        for j in array:
            minHeapInsert(minHeap, j)
        return minHeap
    else:
        return "Error"


def maxHeapInsert(heap, value):
    heap.append(value)
    temp = len(heap) - 1
    while temp > 0:
        parentIndex = getParent(temp)
        if heap[temp] > heap[parentIndex]:
            heap[temp], heap[parentIndex] = heap[parentIndex], heap[temp]
        temp = parentIndex

    return


def minHeapInsert(heap, value):
    heap.append(value)
    temp = len(heap) - 1
    while temp > 0:
        parentIndex = getParent(temp)
        if heap[temp] < heap[parentIndex]:
            heap[temp], heap[parentIndex] = heap[parentIndex], heap[temp]
        temp = parentIndex

    return


def maxHeapPop(heap):
    if len(heap) == 0:
        return
    returnValue = heap[0]
    heap[0] = float("-inf")
    temp = 0
    while getLeftChild(temp, len(heap)) > 0:
        leftChildIndex = getLeftChild(temp, len(heap))
        if getRightChild(temp, len(heap)) > 0:
            rightChildIndex = getRightChild(temp, len(heap))
            if heap[leftChildIndex] > heap[rightChildIndex]:
                heap[temp], heap[leftChildIndex] = heap[leftChildIndex], heap[temp]
                temp = leftChildIndex
            else:
                heap[temp], heap[rightChildIndex] = heap[rightChildIndex], heap[temp]
                temp = rightChildIndex
        else:
            heap[temp], heap[leftChildIndex] = heap[leftChildIndex], heap[temp]
            temp = leftChildIndex
    return returnValue


def minHeapPop(heap):
    if len(heap) == 0:
        return
    returnValue = heap[0]
    heap[0] = float("inf")
    temp = 0
    while getLeftChild(temp, len(heap)) > 0:
        leftChildIndex = getLeftChild(temp, len(heap))
        if getRightChild(temp, len(heap)) > 0:
            rightChildIndex = getRightChild(temp, len(heap))
            if heap[leftChildIndex] < heap[rightChildIndex]:
                heap[temp], heap[leftChildIndex] = heap[leftChildIndex], heap[temp]
                temp = leftChildIndex
            else:
                heap[temp], heap[rightChildIndex] = heap[rightChildIndex], heap[temp]
                temp = rightChildIndex
        else:
            heap[temp], heap[leftChildIndex] = heap[leftChildIndex], heap[temp]
            temp = leftChildIndex
    return returnValue


def getLeftChild(index, length):
    childIndex = index * 2 + 1
    if length >= childIndex + 1:
        return childIndex
    return -1


def getRightChild(index, length):
    childIndex = index * 2 + 2
    if length >= childIndex + 1:
        return childIndex
    return -1


def getParent(index):
    if index % 2 == 0:
        return index // 2 - 1
    else:
        return index // 2


def main():
    array = [i for i in range(30)]
    count = 10
    while count > 0:
        random.shuffle(array)
        print(array)
        print(heapSort(array))
        print(heapSort(array, reverse=True))
        count -= 1
        print()


if __name__ == '__main__':
    main()
