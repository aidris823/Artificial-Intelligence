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
        self.data = list(A)
        if (A is not None):
            self.vals = A
            for i in range(len(A)):
                insert(self,A[i])
    #Gives a new value into the list
    def insert(self,V):
        while i < len(self.data + 1):
            if (self.data[0] is None):
                data[i] = Node(V)
                return
            if (V <= self.data[i].value):
                if (self.data[i].smaller is None):
                    self.data[i].smaller = Node(V)
                else:
                    
                

    #Returns True if value V is inside the list.
    def has(self,V):
        pass
    #Returns ordered list, heap sort
    def get_ordered_list(self):
        pass
    #Sets every node's pointers to other Nodes as None.
    def clear(self):
        pass
        
