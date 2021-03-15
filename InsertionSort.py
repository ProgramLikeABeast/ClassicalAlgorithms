import random


def ISort(array):
    for i in range(len(array)):
        j = i - 1
        while j >= 0:
            if array[j] < array[i]:
                break
            j -= 1
        insert(array, i, j + 1)
    return array


def insert(array, plug, into):
    temp = array[plug]
    for i in reversed(range(into, plug)):
        array[i + 1] = array[i]
    array[into] = temp


def main():
    for i in range(500):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        random.shuffle(array)
        ISort(array)
        print(array)


if __name__ == '__main__':
    main()
