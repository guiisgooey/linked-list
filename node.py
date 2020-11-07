class node: 
    def __init__(self, data):
        """creates a new node object for usage in a linked list"""
        self.data = data
        self.next = None
        self.prev = None #if it's intended for a doubly linked list
