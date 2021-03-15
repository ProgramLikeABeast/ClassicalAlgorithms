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


def RSelectHelper(array, low, high, i):
    if not array[low:high]:
        return
    pivotIndex = partition_pivot_initial(array, low, high)
    if pivotIndex < i:
        return RSelectHelper(array, pivotIndex + 1, high, i)
    elif pivotIndex > i:
        return RSelectHelper(array, low, pivotIndex, i)
    else:
        return array[i]


def RSelect(array, i):
    return RSelectHelper(array, 0, len(array), i-1)


def main():
    for i in range(500):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        random.shuffle(array)
        print(array)
        print(RSelect(array, 8))
    print("To find the 8th largest number in shuffled 1-20.")


if __name__ == "__main__":
    main()
