import random


def merge(array1, array2):
    pointer1 = 0
    pointer2 = 0
    result = []
    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] < array2[pointer2]:
            result.append(array1[pointer1])
            pointer1 += 1
        else:
            result.append(array2[pointer2])
            pointer2 += 1
    if pointer1 == len(array1):
        result += array2[pointer2:]
    else:
        result += array1[pointer1:]
    return result


def mergeSort(array):
    if len(array) < 2:
        return array
    else:
        return merge(mergeSort(array[:len(array) // 2]), mergeSort(array[len(array) // 2:]))


def main():
    for i in range(500):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        random.shuffle(array)
        print(mergeSort(array))


if __name__ == '__main__':
    main()
