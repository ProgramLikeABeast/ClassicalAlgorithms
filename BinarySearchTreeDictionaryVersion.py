import random


class BinarySearchTreeDict:
    def __init__(self):
        self.tree = {}
        self.root = None

    def insert(self, newValue):
        self.tree[newValue] = {'left': None, 'right': None, 'parent': None, 'visited': False}
        if len(self.tree) == 1:
            self.root = newValue
            return
        temp = self.root
        while True:
            if newValue > temp:
                if self.tree[temp]['right'] is not None:
                    temp = self.tree[temp]['right']
                else:
                    self.tree[newValue]['parent'] = temp
                    self.tree[temp]['right'] = newValue
                    return
            else:
                if self.tree[temp]['left'] is not None:
                    temp = self.tree[temp]['left']
                else:
                    self.tree[newValue]['parent'] = temp
                    self.tree[temp]['left'] = newValue
                    return

    def search(self, value):
        temp = self.root
        result = []
        while temp != value:
            if value > temp:
                if self.tree[temp]['right'] is None:
                    return
                temp = self.tree[temp]['right']
                result.append('right')
            else:
                if self.tree[temp]['left'] is None:  # avoid false decision with 0
                    return
                temp = self.tree[temp]['left']
                result.append('left')
        return result

    def findMin(self, start):
        if start not in self.tree:
            return None
        temp = start
        while self.tree[temp]['left'] is not None:
            temp = self.tree[temp]['left']
        return temp

    def findMax(self, start):
        if start not in self.tree:
            return None
        temp = start
        while self.tree[temp]['right'] is not None:
            temp = self.tree[temp]['right']
        return temp

    def findPredecessor(self, value):
        if value not in self.tree:
            return
        if self.tree[value]['left'] is not None:
            leftNode = self.tree[value]['left']
            return self.findMax(leftNode)
        else:
            if value == self.root:
                return
            temp = value
            while self.tree[temp]['parent'] is not None:
                if self.tree[temp]['parent'] < value:
                    return self.tree[temp]['parent']
                temp = self.tree[temp]['parent']
            return

    def findSuccessor(self, value):
        if value not in self.tree:
            return
        if self.tree[value]['right'] is not None:
            rightNode = self.tree[value]['right']
            return self.findMin(rightNode)
        else:
            if value == self.root:
                return
            temp = value
            while self.tree[temp]['parent'] is not None:
                if self.tree[temp]['parent'] > value:
                    return self.tree[temp]['parent']
                temp = self.tree[temp]['parent']
            return

    def outputSorted(self):
        if self.root is None:
            return []
        result = []
        stack = [self.root]
        temp = self.root
        while stack:
            if self.tree[temp]['left'] is not None:
                leftNode = self.tree[temp]['left']
                if not self.tree[leftNode]['visited']:
                    return

    def showMap(self):
        print("root-->" + str(self.root))
        for i in self.tree:
            print(i, end=": ")
            print(self.tree[i])


def main():
    # for i in range(10):
    bst = BinarySearchTreeDict()
    array = [j for j in range(-10, 10)]
    random.shuffle(array)
    array1 = [50, 48, 70, 30, 65, 90, 20, 32, 67,
              98, 15, 25, 31, 35, 66, 69, 94, 99]
    for k in array1:
        bst.insert(k)
    bst.showMap()


if __name__ == '__main__':
    main()
