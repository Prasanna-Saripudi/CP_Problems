# author: Prasanna Saripudi

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        insert(self.root, new_val)

    def insert1(self, root, new_val):
        if root:
            if root.value > new_val:
                if root.left is None:
                    insert1(root.left, new_val)
                else:
                    root.left = new_val
            if root.value < new_val:
                if root.right is None:
                    insert1(root.right, new_val)
                else:
                    root.right = new_val
        else:
            root = new_val
        pass

    def printSelf(self):
        # Your code goes here
        pass

    def search(self, find_val):
        return search1(self.root, find_val)

    def search1(self, root, find_val):
        if root is None or root.value == find_val:
            return True
        if root.value > find_val:
            return search1(root.left, find_val)
        return search1(root.right, find_val)
