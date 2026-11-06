'''
Two way to Print: 
Depth First Search:
    - DFS - iterator / Recursion - Pop from last
    solution deeper within,
    Use stack: FILO

    Inorder: LNR - sorted ascending 
    Preorder: NLR - process root first, copy tree, evaluation
    Postorder: LRN - process subtree first, delete a tree, evaluation

Breadth First Search: 
    BFS - Iterator - Pop from top

    solution closer to root, 
    high to low, level by level, left-right
    Use Queue: FIFO
Level Order: 


'''


# Problem 1: Merging Cookie Orders
'''
Match: Preorder: Node Left Right

Plan:

#recursion way: Basecase
if not cookie1: add cookie2, to new tree
    return cookie2 address
if not cookie2: add cookie1 to new tree
    return cookie1 address

# merge_orders(node)
Node  = TreeNode(cookie1.val + cookie2.val). #node
Node.left = merge_orders(node1.left, node2.left,) #left
Node.right = merge_orders(node1.right,node2.right) #right

return Node

'''
from collections import deque


class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def merge_orders(order1, order2):
    #base case
    if not order1: return order2
    if not order2: return order1

    #recursive case: Preorder NLR
    node = TreeNode(order1.val + order2.val)
    node.left = merge_orders(order1.left, order2.left)
    node.right = merge_orders(order1.right,order2.right)

    return node

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
    

cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

print_tree(merge_orders(order1, order2))
# node = TreeNode(7)
# # print(node)
# <__main__.TreeNode object at 0x000001CAAE8F42F0>
# print(node.val)
# 7

# Problem 2: Croquembouche
'''
-given the root node
-print level by level of each node.val

Plan:
create a list result = []
use queue = [root] #next up list
    #keep track of the children, have ref point of next node go to
    build tree 

while queue:
    node = queue.pop() //(first val from design)
    node.val  -> result  
    
    does Node have child:
        yes result.left: add val to queue
        yes right: add val to queue

return result

'''
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    result = []
    queue = deque()
    
    if design:
        queue.append(design)

    # level = 0
    while queue:
        # for i in range(len(queue)):
        current = queue.popleft()
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        # level += 1
    # print(level)
    return result
            
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(print_design(croquembouche))

# Problem 3: Maximum Tiers in Cake


# Problem 4: Maximum Tiers in Cake II


# Problem 5: Can Fulfill Order
# Problem 6: Icing Cupcakes in Zigzag Order
# Problem Set Version 2