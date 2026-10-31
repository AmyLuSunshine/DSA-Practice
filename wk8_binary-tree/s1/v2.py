# Problem 2: Are Twins?
'''
U
i: tree root(Node root, left, right)
o: T if left val = right val
      else  F
    when root only: return F 
edge: root with one child: return F
P:
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        #self.variable_name, global variable for a class
        self.val = value
        self.left = left
        self.right = right
def mertwins(root):
    if root.left == None or root.right == None:
        return False
    if root.left.val != root.right.val:
        return False
    return True

root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))
root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))
root3 = TreeNode("Merenby", None, TreeNode("Calypso"))

print(mertwins(root1))
print(mertwins(root2))
print(mertwins(root3))


# Problem 8: Ocean Layers
'''
U:
i:root of a binary tree
o:depth/height of tree (count fr root->furthest leaf)

Match: Recursion

P:
Basecase:
if root not exist, 
    return 0 
if node left and right is both none: 
    leaf nodereturn 1
Recursion:

if node.left:
    left += 1 
if node.right:
    right += 1 
return ocean_depth(node.max(left,right))

'''
class TreeNode:
    def __init__(self,value, left=None,right=None):
        self.val = value
        self.left = left
        self.right = right
def ocean_depth(root):
    # base case
    if not root:
        return 0
    else:
        if not root.left and not root.right:
            return 1
    # recursive case
    left = right = 0
    if root.left:
        left = (1 + ocean_depth(root.left))
    if root.right:
        right = (1 + ocean_depth(root.right))
    return max(left,right)
     

ocean = TreeNode("Sunlight", 
                TreeNode("Twilight", 
                        TreeNode("Abyss", 
                                TreeNode("Trenches")), TreeNode("Anglerfish")),
                                        TreeNode("Squid", TreeNode("Giant Squid")))
tidal_zones = TreeNode("Spray Zone", 
                      TreeNode("Beach"), 
                              TreeNode("High Tide", 
                                      TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))
print(ocean_depth(tidal_zones))


