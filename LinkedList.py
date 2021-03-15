class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insertFirst(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def insertLast(self, value):
        node = Node(value)
        self.length += 1
        if self.isEmpty():
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def pop(self):
        temp = self.head
        if not temp:
            return
        if not temp.next:
            result = self.head.value
            self.head = None
        else:
            while temp.next.next:
                temp = temp.next
            result = temp.next.value
            temp.next = None
        self.length -= 1
        return result

    def peek(self):
        temp = self.head
        if not temp:
            return
        if not temp.next:
            return self.head.value
        else:
            while temp.next.next:
                temp = temp.next
            return temp.next.value

    def isEmpty(self):
        return self.head is None

    def length(self):
        return self.length

    def show(self):
        temp = self.head
        while temp:
            print(temp.value, end='-')
            temp = temp.next
        print()


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, value):
        self.insertLast(value)


class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, value):
        self.insertFirst(value)


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())


if __name__ == '__main__':
    main()
