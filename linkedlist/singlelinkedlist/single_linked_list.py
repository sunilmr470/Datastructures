"""
Single linkedlist Implementation
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            prev_node = self.head
            while prev_node.next:
                prev_node = prev_node.next
            prev_node.next = node

    def print_list(self):
        if not self.head:
            print("Empty list")
            return
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def insert_at_starting(self, data):
        node = Node(data)
        cur_node = self.head
        self.head = node
        self.head.next = cur_node

    def delete_an_element(self, ele):
        cur_node = self.head
        if not cur_node:
            raise Exception("Empty list")
        while cur_node.next and cur_node.data != ele:
            prev_node = cur_node
            cur_node = cur_node.next
        upcoming_node = cur_node.next
        prev_node.next = upcoming_node

    def len(self):
        c = 0
        cur_node = self.head
        while cur_node:
            c += 1
            cur_node = cur_node.next
        print(c)

    def insert_at_specific_index(self, index, data):
        node = Node(data)
        cur_node = self.head
        c = 0
        while cur_node and c != index:
            c += 1
            prev_node = cur_node
            cur_node = cur_node.next
        node.next = cur_node
        prev_node.next = node


if __name__ == "__main__":
    l = SingleLinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.insert_at_specific_index(4, 8)
    l.print_list()
