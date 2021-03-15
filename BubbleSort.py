import random


def BSort(array):
    for i in reversed(range(len(array))):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def main():
    for i in range(500):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        random.shuffle(array)
        BSort(array)
        print(array)


if __name__ == '__main__':
    main()
