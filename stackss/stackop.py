from stack import *

stack=Stack()
stack.push(4)
stack.push(5)
stack.pushexp("abcdef")
stack.peek()
stack.pop()
print(stack.get_length())
stack.print_stack()
stack.delete()