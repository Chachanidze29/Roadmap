class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def prepend(self, value):
        new_node = self.Node(value, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def append(self, value):
        new_node = self.Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next_node = new_node
        self.tail = new_node

    def map(self, callback):
        head = self.head
        while head is not None:
            callback(head.value)
            head = head.next_node

    def search(self, value):
        head = self.head
        while head is not None:
            if head.value == value:
                return True
            head = head.next_node
        return False

    def pop(self):
        if not self.head:
            return None
        value = self.head.value
        if self.head.next_node:
            self.head = self.head.next_node
        else:
            self.head = None
            self.tail = None
        return value

    def pop_back(self):
        curr = self.head
        while curr.next_node.next_node is not None:
            curr = curr.next_node
        value = curr.next_node.value
        curr.next_node = None
        self.tail = curr
        return value

    def len(self):
        count = 0
        head = self.head
        if head is None:
            return 0
        while head is not None:
            count += 1
            head = head.next_node
        return count


if __name__ == '__main__':
    pass