
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.stack = []
        self.max_value = float('-inf')

    def push(self, value):
        """Push a new item to the stack"""
        if value > self.max_value:
            self.max_value = value
        self.stack.append(value)

    def pop(self):
        """Remove the last item in the stack"""
        if not self.stack:
            raise BaseException("EmptyStackError")

        last_item_to_be_removed = self.stack[-1]
        self.stack = self.stack[0:-1]
        return last_item_to_be_removed

    def peek(self):
        """Return the last item without removing it"""
        return self.stack[-1]

class MaxStack(Stack):
    def __init__(self):
        super().__init__()

    def get_max(self):
        return self.max_value

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    print(stack.peek())
    print(stack.stack)

    maxStack = MaxStack()
    maxStack.push(99)
    print(maxStack.get_max())

