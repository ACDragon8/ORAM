import secrets
from array import array

class Bucket:
    def __init__(self, data, a, x):
        self.data = data
        self.a = a
        self.x = x

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self,value):
        if (self.left == None):
            self.left = Node(value)
            return True
        elif (self.right == None):
            self.right = Node(value)
            return True
        else:
            return False
    def draw(self):
        print(self.value, end = ',')
        if (self.left != None):
            self.left.draw()
        if (self.right != None):
            self.right.draw()
        
    def is_full(self):
        return not ((self.left == None) or (self.right == None))



class Tree:
    def __init__(self):
        self.head = None
    def add(self, value):
        if (self.head == None):
            self.head = Node(value)
        else:
            nodes = [self.head]
            a = nodes[0].add(value)
            while (not a):
                nodes.append(nodes[0].left)
                nodes.append(nodes[0].right)
                nodes.pop(0)
                a = nodes[0].add(value)

    def create(self, n):
        for i in range(2 ** n-1):
            self.add(i)
    def draw(self):
        if (self.head == None):
            return
        else:
            nodes = [self.head]
            while (len(nodes) >= 1):
                print(nodes[0].value)
                if (nodes[0].left != None):
                    nodes.append(nodes[0].left)
                if (nodes[0].right != None):
                    nodes.append(nodes[0].right)
                nodes.pop(0)


        


        

    
