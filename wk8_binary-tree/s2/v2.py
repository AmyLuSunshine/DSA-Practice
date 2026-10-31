'''# Problem 2: Searching Ariel's Treasures
'''






'''
from collections import deque 

# Tree Node class
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def build_tree(values):
  if not values:
      return None

#   def get_key_value(item):
#       if isinstance(item, tuple):
#           return item[0], item[1]
#       else:
#           print(item)
#           return None, item
       
  value = values[0]
  root = TreeNode(value)
  queue = deque([root])
  index = 1
  
  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_value = values[index]
          node.left = TreeNode(left_value)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_value = values[index]
          node.right = TreeNode(right_value)
          queue.append(node.right)
      index += 1

  return root



         
def locate_treasure(grotto, treasure):
    #base case
    if not grotto:
        return False
    if grotto and grotto.val == treasure:
        return True
    #recursion case
    if grotto and grotto.val > treasure:
        if grotto.left:
            locate_treasure(grotto.left, treasure)
    elif grotto and grotto.val < treasure:
        if grotto.right:
            locate_treasure(grotto.right, treasure)
    else:
        return True


values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]
grotto = build_tree(values)

print(locate_treasure(grotto, "Dinglehopper"))  
print(locate_treasure(grotto, "Thingamabob")) '''

# Problem 2: Searching Ariel's Treasures
'''
U


P


'''
from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
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

"""
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
"""
         
def locate_treasure(grotto, treasure):
    # Base case
    if not grotto:
        return False

    # print("Grotto Key: ", grotto.key, " | Grotto Value: ", grotto.val, " | Treasure: ", treasure)

    if grotto and grotto.val == treasure:
        # print("Treasure found")
        return True

    # Recursive cases
    if grotto and grotto.val > treasure:
        return locate_treasure(grotto.left, treasure)
    elif grotto and grotto.val < treasure:
        return locate_treasure(grotto.right, treasure)


values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]
grotto = build_tree(values)

print(locate_treasure(grotto, "Dinglehopper")) # --> Expected: True | Actual: None
print(locate_treasure(grotto, "Thingamabob"))  # --> Expected: False | Actual: None