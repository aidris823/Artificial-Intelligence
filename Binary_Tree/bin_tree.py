import math

class Node:
    def __init__(self,data):
        self.value = data
        self.smaller = None
        self.larger = None
    def __str__(self):
        return str(self.value)

class BinTree:
    def __init__(self,A=None):
        self.root = None
        if (A is not None):
            for i in range(len(A)):
                insert(self,A[i])
    #Gives a new value into the list
    def insert(self,V):
        insert(self,V,0)
        """
        while i < len(self.data + 1):
            if (self.data[0] is None):
                data[i] = Node(V)
                return
            if (V <= self.data[i].value):
                if (self.data[i].smaller is None):
                    self.data[i].smaller = Node(V)
                else:
           """
    def insert(self, V, level):
        if self.data[level] is None:
            leaf = Node(V)
            

    #Returns True if value V is inside the list.
    def has(self,V):
        pass
    #Returns ordered list, heap sort
    def get_ordered_list(self):
        pass
    #Sets every node's pointers to other Nodes as None.
    def clear(self):
        pass
        
