# Queue implementation using list

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        print(self.queue)

    # Peek element
    def peek(self):
        if len(self.queue) < 1:
            return None
        return self.queue[0]

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Clear the queue (remove all elements)
    def clear(self):
        self.queue = []

    # Get the size of the queue
    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(10)

print("Queue after adding element:")
print("Peek element :", q.peek())

q.display()

q.dequeue()

print("Queue after removing element:")
q.display()




