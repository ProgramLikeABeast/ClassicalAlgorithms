import random


def partition_pivot_initial(array, low, high):
    if len(array) <= 1:
        return -1
    else:
        i = low + 1
        for j in range(low + 1, high):
            if array[j] < array[low]:
                array[i], array[j] = array[j], array[i]  # swap
                i = i + 1
        array[low], array[i - 1] = array[i - 1], array[low]
        return i - 1


def quickSortHelper(array, low, high):
    if not array[low:high]:
        return
    pivotIndex = partition_pivot_initial(array, low, high)
    if pivotIndex >= 0:
        quickSortHelper(array, low, pivotIndex)
        quickSortHelper(array, pivotIndex + 1, high)


def quickSort(array):
    quickSortHelper(array, 0, len(array))
    return array


def main():
    for i in range(500):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        random.shuffle(array)
        print(quickSort(array))


if __name__ == '__main__':
    main()
