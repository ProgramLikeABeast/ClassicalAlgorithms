import random


def BruteForceSearch(array):
    count = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                count += 1
    return count


def countSplitInv(array1, array2):
    k = len(array1) + len(array2)
    left = 0
    right = 0
    exist = 0
    inverse = 0
    result = []
    while k >= 0:
        if array1[left] < array2[right]:
            result.append(array1[left])
            inverse += exist
        else:
            result.append(array2[right])
            exist += 1
    return [result, inverse]


def countInv(array):
    if len(array) == 0 or len(array) == 1:
        return 0
    else:
        leftPart = array[:len(array) // 2]
        rightPart = array[len(array) // 2:]
        return countInv(leftPart) + countInv(rightPart) + countSplitInv(leftPart, rightPart)


def main():
    group = [i for i in range(20)]
    for i in range(10):
        random.shuffle(group)
        print(group)
        print("Brute Force:" + str(BruteForceSearch(group)))


if __name__ == '__main__':
    main()
