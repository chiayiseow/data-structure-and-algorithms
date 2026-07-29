
# question link: https://www.interviewcake.com/question/python3/queue-two-stacks?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23617:%20Implement%20A%20Queue%20With%20Two%20Stacks&utm_medium=email&utm_medium=email&__s=nywctklrkfaexchucj9e

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

class SpecialQueue:
    def __init__(self):
        stack1 = Stack()
        stack2 = Stack()
        self.stack1 = stack1
        self.stack2 = stack2

    def enqueue(self, value):
        self.stack1.push(value)
    
    def dequeue(self):
        for times in range(len(self.stack1.stack)):
            removed = self.stack1.pop()
            self.stack2.push(removed)
        new_last_item = self.stack2.stack[-1]
        self.stack2.stack = self.stack2.stack[:-1]
        self.stack1.stack = self.stack2.stack[::-1]
        return new_last_item

if __name__ == "__main__":
    queue = SpecialQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.enqueue(4)
    print(queue.stack1.stack)