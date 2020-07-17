# author: Prasanna Saripudi
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.root and isinstance(find_val, int):
            bool = self.preorder_search(self.root, find_val)
            return bool
        else:
            return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        self.preorder_print(self.root)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start == None:
            return False
        if start.value == find_val:
            return True
        leftcheck = self.preorder_search(start.left, find_val)
        if leftcheck:
            return True
        rightcheck = self.preorder_search(start.right, find_val)
        return rightcheck

    def preorder_print(self, start):
        """Helper method - use this to create a 
        recursive print solution. """
        if start:
            print(str(start.value) + " ")
            self.preorder_print(start.left)
            self.preorder_print(start.right)
