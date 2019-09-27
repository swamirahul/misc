https://www.koderdojo.com/blog/inorder-traversal-of-binary-search-tree-in-python
from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(node, root):
    if root is None:
        raise ValueError('root cannot be None.')

    nodes_found = deque([root])

    while len(nodes_found) > 0:
        current_node = nodes_found.popleft()

        if current_node.left is None:
            current_node.left = node
            break
        if current_node.right is None:
            current_node.right = node
            break

        nodes_found.append(current_node.left)
        nodes_found.append(current_node.right)
        
        
root = Node(8)
keys = [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

for key in keys:
    add(Node(key), root)



def display_nodes(root):
    if root is None:
        return

    if root.left is not None:
        display_nodes(root.left)

    print(root.key, end=' ')

    if root.right is not None:
        display_nodes(root.right)
        
        
        
 display_nodes(root)
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
