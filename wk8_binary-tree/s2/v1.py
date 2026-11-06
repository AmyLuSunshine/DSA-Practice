# Problem 1: Monstera Madness
'''
Understand:
input: root node of a binary tree
output: one int ( the sum of the odd nodes )

Plan:
Basecase:
if root is empty: return 0
if the node number is odd: return 1
if the node number is even: return 0
Recursion case:
return count_odd_splits(root.left) + count_odd_splits(root.left)
'''
from collections import deque

class TreeNode():
     def __init__(self, value, left=None, right=None):
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
         
def count_odd_splits(root):
    count = 0

    if not root:
        return 0
    if root.val % 2 != 0:
        count = 1
    # else:  # use else, or just create variable on top count = 0
    #     count = 0

    return count + count_odd_splits(root.left) + count_odd_splits(root.right)

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))


# Problem 2: Flower Finding


# Problem 3: Flower Finding II



# Problem 4: Adding a New Plant to the Collection


# Problem 5: Sorting Plants by Rarity
'''
Understand:
input: root(tuple(num, str))
output: sorted binary tree

Plan:
Inorder: L root R - Inorder traversal, to solve for BST
Preorder: root L R - duplicate the tree, make a copy
Postorder: L R root - calculate height/size of the tree

create a variable: sorted_collection = []

Build a helper function: 
def in_order(node)
    Basecase:
    if not node: return

    Recursion case:
    in_order(node.left)
    sorted_collection.append(node.key, node.val)
    in_order(node.right)
    
in_order(collection)

return sorted_collection


'''
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = value      # Plant name
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

    #     # Build a helper function: 
    # def in_order(node):
    #     # create a variable: 
    #     sorted_collection = []
    #     #     Basecase:
    #     if not node: return

    #     # Recursion case:
    #     in_order(node.left)
    #     sorted_collection.append((node.key, node.val))
    #     in_order(node.right)

    # def sort_plants(collection):
    
    #     res = in_order(collection)

    #     return res
    def sort_plants(collection):
        result = []
    
    def inorder(node):
        if node is not None:
            inorder(node.left)
            result.append((node.key, node.val))
            inorder(node.right)
    
    inorder(collection)
    return result

values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))

# Problem 6: Finding a New Plant Within Budget



# Problem 7: Remove Plant