class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, obj):
        new_node = Node(obj)
        if self.top == None:
            self.top = new_node
            self.size += 1
        else:
            new_node.prev = self.top
            self.top = new_node
            self.size += 1
        return new_node.data

    def pop(self):
        if self.size == 0:
            return
        elif self.size == 1:
            self.top = None
            self.size -= 1
        else:
            tmp = self.top
            self.top = self.top.prev
            tmp.prev = None
            self.size -= 1
            return self.top.data

    def top(self):
        if self.top != None:
            return self.top.data


    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def empty(self):
        self.top = None
        self.size = 0

    def print_stack(self):
        curr = self.top
        while curr != None:
            print(curr.data)
            curr = curr.prev


