# Q1 
'''
Understand:
- Input: Head of linked List,
- Output: boolean
- Edge cases: null head -> return False, looped LL not at head -> False

Match:
- Linked List

Plan:
- check edge cases
- current = head
- loop through each node
- check if node is in a set of nodes
- if node is not, we add node to set, move current to next node
- if node is in set or next of node = None -> reached the end 
- is that next node = head return True, else False

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    head = clues
    slow = clues
    fast = clues
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast and slow == head:
            return True
        elif slow == fast and slow != head:
            return False
    return False
        
clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))
'''
"""
Understand:
Input: head of a node
Output: an array 

Match:
We get head of a linked liist as an argument, 
and we return the values of the nodes in a circular loop,
as unorder arrays

- use fast and slow pointer to find a loop
- when loop found append an array with the values of the nodes in it
- return the list with the values
- if loop terminates return an empty list

-> if input is none return empty list
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    if not evidence:
        return []
    slow = evidence
    fast = evidence
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        curr = slow
        if slow == fast:
            result = []
            while slow != curr.next:
                result.append(curr.value)
                curr = curr.next
            return result
    return []


clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))


"""
Understand:
Input: head of a node with a group of nums , and a threshod #
      reorder the nums>threshold infront, then threshod, then put nums<threshold
Output: head of the reordered linklist 

Plan:
temp head / dummy head -> head
curr -> head

T
4 -> 5 -> 1 -> 3 -> 2 -> 2
               P    
          C


"""