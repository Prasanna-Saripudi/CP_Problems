"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""
# author: Prasanna Saripudi


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000
        print("object created")

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
        self.table.append(string)

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        if string in self.table:
            hash = self.calculate_hash_value(string)
            return hash
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # ord(charac) = > asciiValue
        # chr(ascii) => character
        return (ord(string[0])*100)+ord(string[1])
