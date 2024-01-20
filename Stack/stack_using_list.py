# Stack implementation using list 

# Creating a stack
def create_stack():
    stack = []
    return stack

# Checking if the stack is empty
def is_empty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("Pushed item: " + item)

# Removing an element from the stack
def pop(stack):
    if is_empty(stack):
        return "Stack is empty"
    return stack.pop()

# Viewing the top element without removing it
def peek(stack):
    if is_empty(stack):
        return "Stack is empty"
    return stack[-1]

# Getting the size of the stack
def size(stack):
    return len(stack)

# Displaying the elements of the stack without removing them
def display(stack):
    return stack

# Example usage
stack = create_stack()

push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
push(stack, str(6))
push(stack, str(7))
push(stack, str(10))

print("Peeked item: " + peek(stack))
print("Stack size: " + str(size(stack)))
print("Stack after pushing element: " + str(display(stack)))

pop(stack)
pop(stack)
pop(stack)
print("Stack after popping an element: " + str(display(stack)))
