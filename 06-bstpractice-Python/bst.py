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
        self.insert1(self.root, new_val)

    def insert1(self, root, new_val):
        # recursive helper function for inserting
        if root:
            if root.value > new_val:
                if root.left is not None:
                    self.insert1(root.left, new_val)
                else:
                    root.left = Node(new_val)
            elif root.value < new_val:
                if root.right is not None:
                    self.insert1(root.right, new_val)
                else:
                    root.right = Node(new_val)
        else:
            root = Node(new_val)

    def printSelf(self):
        self.printSelf1(self.root)

    def printSelf1(self, root):
        # recursive iterative dunction for print
        if root is None:
            return
        print(" ", root.value)
        self.printSelf1(root.left)
        self.printSelf1(root.right)

    def search(self, find_val):
        if self.root and isinstance(find_val, int):
            root = self.search1(self.root, find_val)
            f = True if root else False
            print(f)
            return True if root else False
        return False

    def search1(self, root, find_val):
        # recursive iterative function for searching
        if root is None or root.value == find_val:
            print("in middle")
            return root
        if root.value > find_val:
            print("in left")
            return self.search1(root.left, find_val)
        if root.value < find_val:
            print("in right")
            return self.search1(root.right, find_val)
