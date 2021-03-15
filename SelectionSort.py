import random


def SSort(array):
    for i in range(len(array)):
        target = min(array[i:])
        for j in range(i, len(array)):
            if array[j] == target:
                array.pop(j)
                break
        array.insert(i, target)
    return array


def main():
    for i in range(500):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        random.shuffle(array)
        SSort(array)
        print(array)


if __name__ == '__main__':
    main()
