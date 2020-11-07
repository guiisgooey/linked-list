from music_playlist import music_playlist
from node import node

playlist = music_playlist()

s0 = node("santeria")
s1 = node("gangster's paradise")
s2 = node("walkin' on the sun")
s3 = node("automation")
s4 = node("cyboogie")

s1.next = s2
s2.next = s3

playlist.head = s1
playlist.tail = s3

playlist.print_songs()

playlist.append(s4)
playlist.prepend(s0)

playlist.print_songs()

playlist.delete_from_head()
playlist.delete_from_tail()

playlist.print_songs()

print(playlist.find("automation"))
print(playlist.delete("automation"))

playlist.print_songs()

playlist.reverse()
playlist.print_songs()