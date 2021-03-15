class BinaryNode:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, newValue):
        newNode = BinaryNode(newValue)
        self.size += 1
        if self.size == 1:
            self.root = newNode
            return
        temp = self.root
        while True:
            if newValue > temp.value:
                if temp.right:
                    temp = temp.right
                else:
                    newNode.parent = temp
                    temp.right = newNode
                    return
            else:
                if temp.left:
                    temp = temp.left
                else:
                    newNode.parent = temp
                    temp.left = newNode
                    return


def main():
    array = [i for i in range(30)]
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(0)
    print(bst.root.value)
    print(bst.root.left.value)
    print(bst.root.right.value)


if __name__ == '__main__':
    main()
