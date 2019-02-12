import math

class Node:
    def __init__(self,data):
        self.value = data
        self.smaller = None
        self.larger = None
    def __str__(self):
        return str(self.value)
