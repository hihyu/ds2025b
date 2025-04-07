class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "Stack is empty!"
        popped_node = self.top
        self.top = self.top.link
        return popped_node.data


s1 = list()
print(len(s1))
s1.append("Data structure")  # push
s1.append("DataBase")  # push
print(len(s1))  # size
print(s1[-1])  # peek
print(s1)
print(s1.pop())
print(s1)
print(s1.pop())
print(s1)
# print(s1.pop())
# print(s1)