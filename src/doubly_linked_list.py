class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, value, next_node=None, prev_node=None):
            self.value = value
            self.next_node = next_node
            self.prev_node = prev_node

    def prepend(self, value):
        new_node = self.Node(value)
        if self.head is not None:
            self.head.prev_node = new_node
            new_node.next_node = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next_node = new_node
        new_node.prev_node = self.tail
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
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next_node
        self.head.prev_node = None
        return value

    def pop_back(self):
        if self.head is None:
            return None
        value = self.tail.value
        new_tail = self.tail.prev_node
        new_tail.next = None
        new_tail.prev_node = self.tail.prev_node.prev_node
        self.tail = new_tail
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

