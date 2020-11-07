from music_playlist import music_playlist
from node import node


playlist = music_playlist()


n0 = node(0)
n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)

n1.next = n2
n2.next = n3

playlist.head = n1
playlist.tail = n3


playlist.print_songs()

playlist.append(n4)
playlist.prepend(n0)

playlist.print_songs()

playlist.delete_from_head()
playlist.delete_from_tail()

playlist.print_songs()

print(playlist.find(3))
print(playlist.delete(3))

playlist.print_songs()

playlist.reverse()
playlist.print_songs()