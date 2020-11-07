class music_playlist:
    def __init__(self):
        """creates a new music playlist linked list object"""
        self.head = None
        self.tail = None

    def append(self, song):
        """inserts a new item in the linked list at the end of the list, making it the tail"""
        self.tail.next = song
        self.tail = song
        
    def prepend(self, song):
        """inserts a new item in the linked list at the front of the list, making it the head"""
        song.next = self.head
        self.head = song

    def print_songs(self):
        """prints all songs in the music playlist"""
        current = self.head
        while current is not None:
            print (current.data)
            current = current.next

    def delete_from_head(self):
        """removes head of the linked list, making the second item the new head"""
        self.head = self.head.next

    def delete_from_tail(self):
        """removes tail of the linked list, making the next to last item the new tail"""
        current = self.head
        while current.next is not None:
            if current.next.next is None:
                current.next = None
            else:
                current = current.next
    
    def delete_from_tail2(self):
        """removes tail of the linked list, making the next to last item the new tail
        for usage in doubly linked lists only"""
        self.tail = self.tail.prev

    def find(self, item):
        """finds specified item if it is in the linked list. Returns index if found, -1 if not"""
        current = self.head
        counter = 0
        while current is not None:
            if current.data == item:
                return counter
            elif current.next is not None:
                current = current.next
                counter += 1
            else:
                return -1

    def delete(self, item):
        """deletes specified item if it is in the linked list. Returns true if deleted, false if not deleted"""
        current = self.head
        deleted = False
        if current.data == item:
            self.delete_from_head()
            deleted = True
        else:
            while current.next is not None:
                if current.next.data == item:
                    current.next = current.next.next
                    deleted = True
                else:
                    current = current.next
        return deleted

    def reverse(self):
        """reverses the linked list making the head the tail and the tail the head and reverses the placement of everything inbetween"""
        previous = None
        current = self.head
        self.tail = current
        while current is not None:
            nextTemp = current.next
            current.next = previous
            previous = current
            current = nextTemp
        self.head = previous
