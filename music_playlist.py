class music_playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, song):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = song

    def prepend(self, song):
        song.next = self.head
        self.head = song

    def print_songs(self):
        current = self.head
        while current is not None:
            print (current.data)
            if current.next is not None:
                current = current.next
            else:
                break

    def delete_from_head(self):
        self.head = self.head.next

    def delete_from_tail(self):
        current = self.head
        while current.next is not None:
            if current.next.next is None:
                current.next = None
            else:
                current = current.next

    def find(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return current.data
            elif current.next is not None:
                current = current.next
            else:
                return -1

    def delete(self, item):
        current = self.head
        deleted = False
        if current.data == item:
            self.delete_from_head()
        else:
            while current.next is not None:
                if current.next.data == item:
                    current.next = current.next.next
                    deleted = True
                else:
                    current = current.next
        return deleted

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            nextTemp = current.next
            current.next = previous
            previous = current
            current = nextTemp
        return previous

