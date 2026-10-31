# Problem 9: Tom and Jerry
"""
U:
linkedlist node provided. create two nodes, cat -> mouse
cat.value = "Tom", cat.next = mouse & mouse.value = "Jerry"


P:

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

mouse = Node("Jerry")
cat = Node("Tom", mouse)

print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next)

# Problem 10: Chase List


print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
print(mouse.next.value)