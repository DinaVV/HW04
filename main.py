from collections import deque


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    # Task 1
    def clear(self):
        current = self.head
        while current:
            next_node = current.next  # move next node
            # delete the current node
            del current.data
            del current.next
            current = next_node
            self.size -= 1
        self.head = None

    # Task2
    def get_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return data
            current = current.next
        return False

    # Task3
    def delete(self, data):
        prev = self.head
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next


singly_linked_list = SinglyLinkedList()
singly_linked_list.append("Node1")
singly_linked_list.append("Node2")
singly_linked_list.append("Node3")
singly_linked_list.append("Node4")
singly_linked_list.append("Node5")

for val in singly_linked_list:
    print(val)

print(singly_linked_list.get_data("Node3"))
print(singly_linked_list.get_data("Node6"))

singly_linked_list.delete("Node3")
for val in singly_linked_list:
    print(val)

singly_linked_list.delete("Node5")
for val in singly_linked_list:
    print(val)

singly_linked_list.clear()
for node in singly_linked_list:
    print(node.data)


# Task4
class NodeDLL:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def append(self, data):
        node = NodeDLL(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            # Task4
            node.previous = current
            self.tail = node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def clear(self):
        current = self.head
        while current:
            next_node = current.next  # move next node
            # delete the current node
            del current.data
            del current.next
            current = next_node
            self.size -= 1
        self.head = None

    def get_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return data
            current = current.next
        return False

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        if self.tail.data == data:
            self.tail = self.tail.previous
        prev = self.head
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                current.next.previous = prev
                self.size -= 1
                return
            prev = current
            current = current.next


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("NodeDLL1")
doubly_linked_list.append("NodeDLL2")
doubly_linked_list.append("NodeDLL3")
doubly_linked_list.append("NodeDLL4")
doubly_linked_list.append("NodeDLL5")
for val in doubly_linked_list:
    print(val)

doubly_linked_list.delete("NodeDLL4")
for val in doubly_linked_list:
    print(val)

print("I'm the Queen")


# Task5


class MyStack:

    # Constructor creates a deque, which is a DLL in python, and more efficient to use here
    def __init__(self):
        self.stack = deque()

    # Adding elements to stack
    def push(self, data):
        # Checking to avoid duplicate entries
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False

    # Removing last element from the stack from the right
    def pop(self):
        if len(self.stack) <= 0:
            return "Stack Empty!"
        return self.stack.pop()

    # Getting the last element of the list
    def top(self):
        if self.size() > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return "Stack Empty!"

    # Getting the size of the stack (length of the list)
    def size(self):
        return len(self.stack)


my_queue = MyStack()
print(my_queue.push(5))  # print True
print(my_queue.push(6))  # print True
print(my_queue.push(9))  # print True
print(my_queue.push(5))  # print False as 5 is there
print(my_queue.push(3))  # print True
print(my_queue.size())  # prints 4
print(my_queue.pop())  # prints 3
print(my_queue.pop())  # prints 9
print(my_queue.top())  # prints 6
print(my_queue.pop())  # prints 6
print(my_queue.pop())  # prints 5
print(my_queue.size())  # prints 0
print(my_queue.pop())  # prints Stack Empty!
print(my_queue.top())  # prints Stack Empty! here


# Task6

class MyQueue:

    # Constructor creates a deque, which is a DLL in python, and more efficient to use here
    def __init__(self):
        self.queue = deque()

    # Adding elements to stack to the right
    def push(self, data):
        # Checking to avoid duplicate entries
        if data not in self.queue:
            self.queue.append(data)
            return True
        return False

    # Removing last element from the stack from the left
    def pop(self):
        if len(self.queue) <= 0:
            return "MyQueue Empty!"
        return self.queue.popleft()

    # Getting the last and first elements of the list
    def show_left(self):
        if self.size() > 0:
            return self.queue[0]
        else:
            return "MyQueue Empty!"

    def show_right(self):
        if self.size() > 0:
            return self.queue[len(self.queue) - 1]
        else:
            return "MyQueue Empty!"

    # Getting the size of the stack (length of the list)
    def size(self):
        return len(self.queue)


my_queue = MyQueue()
print(my_queue.push(5))  # print True
print(my_queue.push(6))  # print True
print(my_queue.push(9))  # print True
print(my_queue.push(5))  # print False as 5 is there
print(my_queue.push(3))  # print True
print(my_queue.size())  # prints 4
print(my_queue.pop())  # prints 5
print(my_queue.pop())  # prints 6
print(my_queue.show_left())  # prints 9
print(my_queue.show_right()) # prints 3
print(my_queue.pop())  # prints 9
print(my_queue.pop())  # prints 3
print(my_queue.size())  # prints 0
print(my_queue.pop())  # prints Queue Empty!

