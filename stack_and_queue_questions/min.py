# How would you design a stack which, in addition to push and pop, has a min function which returns the min element? PUSH, POP, AND MIN ALL SHOULD OPERATE IN O(1)


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        string = str(self.val)

        if self.next:
            string += " -> " + str(self.next.val)

        return string


class LinkedStack:
    def __init__(self):
        self.top = None
        self.min_node = None

    def min(self):
        if not self.min_node:
            return None
        return self.min_node.val

    def push(self, item):
        if self.min_node and (self.min_node.val < item):
            self.min_node = Node(val=self.min_node.val, next=self.min_node)
        else:
            self.min_node = Node(val=item, next=self.min_node)

        self.top = Node(val=item, next=self.top)

    def pop(self):
        if not self.top:
            return
        self.min_node = self.min_node.next
        item = self.top.val
        self.top = self.top.next
        return item


custom_stack = LinkedStack()

custom_stack.push(10)
custom_stack.push(11)
print(custom_stack.min())
custom_stack.push(5)

print(custom_stack.min())


custom_stack.pop()
print(custom_stack.min())


custom_stack.push(22)
custom_stack.push(21)
custom_stack.push(2145)

print(custom_stack.min())