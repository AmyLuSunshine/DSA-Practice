#Problem 1: Building a playlist

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

# Problem 2: Top Artists    
'''
define the function name
define a traverse node
define result dictionary
start with the head and use a while loop to traverse the list
until the head is None

if the head's artist is in the dictionary then add 1 to the count
if the head's artist is not in the dictionary then add it to the dictionary and set it to 1
return the resulting dictionary
'''
'''
def get_artist_frequency(playlist):
    result = {}
    traverse = playlist
    while traverse is not None:
        if traverse.artist in result:
            result[traverse.artist] += 1
        else:
            result[traverse.artist] = 1
        traverse = traverse.next
    return result

# Problem 3: Glitching Out
def remove_song(playlist_head, song):
    if not playlist_head: # if no input
        return None
    if playlist_head.song == song: # if first input is song wanting to remove
        return playlist_head.next

    current = playlist_head
    while current.next: # O(n)
        if current.next.song == song:
            current.next = current.next.next  # changed from curr = curr.next.next
            return playlist_head 
        current = current.next
    
    return playlist_head
    # O(1) Space
    # O(n) time
'''    
# Problem 4: On Repeat 
"""
input: head of LL,
output: T if cycle, F if no cycle
Cycle LL: node.next -> previous node

Two Pointers:
Sp: Playlist, go one by one
Fp: pointer go two by two, move twice

if sp == fp: there's cycle return T
otherwise return F

"""
'''
def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head
    
    while fast and fast.next:#check if there's next before skip it
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Problem 5: Looped
def loop_length(playlist_head):
    slow = fast = playlist_head
    count = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            curr = slow.next
            count = 1
            
            while curr != slow:
                curr = curr.next
                count += 1
            return count
    return 0
'''

"""
U:
i:ll_head
m:
    fp=sp=head
    fp+=2
    sp+=1
O:length of cycle, or 0 if no cycle 
    define a cycle: when s==f

 w s q l
 
P:

while f and f.n: # stop when none 
    fp+=2
    sp+=1
    if s == f:  # stop when yes cycle
        curr = s.next
        count = 1
        while curr != s:
            count += 1
            curr = curr.next
            if curr == s
        return count
return 0
        

"""
class SongNode:
    def __init__(self, song, artist, next=None)
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    pass





# Problem 6:Volume Control

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
"""
traverse through list
prev pointer so we can compare with prev and next
if curr is greater than both local max, if curr is less than both curr is local min
increase count if either.
"""
def count_critical_points(song_audio):
    if not song_audio or not song_audio.next:
        return 0
    
    count = 0
    prev, curr = song_audio, song_audio.next
    
    while curr.next:
        next_val = curr.next.value
        
        is_min = curr.value < prev.value and curr.value < next_val
        is_max = curr.value > prev.value and curr.value > next_val
        
        if is_min or is_max:
            count += 1
        
        prev = curr
        curr = curr.next
        
    return count

"""        
top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

print_linked_list(top_hits_2010s)
"""
playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))
# print(get_artist_frequency(playlist))
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))
"""
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))
"""
"""
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))
"""
song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))