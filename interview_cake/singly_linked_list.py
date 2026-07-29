class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def contains_cycle(node):
    prev = node
    next_node = node.next
    if next_node.next == prev:
        return True
    
    return False
if __name__ == "__main__":
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node1.next = node2
    node2.next = node1
    print(contains_cycle(node1))