# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self,b,h):
        self.base = float(b)
        self.height = float(h)
    def area(self):
        return 1/2.0*self.base*self.height
    def __str__(self):
        return 'Triangle with base '+ str(self.base)+' and height '+ str(self.height)
    def __eq__(self,other):
        return type(other) == Triangle and self.base == other.base and self.height == other.height

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.set = []
        self.place = None
     
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        for shape in self.set:
            if sh == shape:
                raise ValueError('no two shapes in the set may be equal')
        self.set.append(sh)
       
                    
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place = 0
        return self

    def next(self):
        if self.place >= len(self.set):
            raise StopIteration
        self.place += 1
        return self.set[self.place-1]
        ## TO DO

    
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        str=''
        for sh in sorted(self.set):
            str+=sh.__str__()+'\n'
        return str
           
  
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """   
    list_of_areas = []
    for shape in shapes:
        list_of_areas.append(shape.area())

    result=[]
    m = max(list_of_areas)
    for i in shapes:
        if i.area()==m:
            result.append(i)

    return tuple(result)
            
        
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
   
    shapes = ShapeSet()
    inputFile = open(filename)
    for line in inputFile:
        line=line.strip().split(",")
        if line[0]=='square':
            shape = line[0]
            side = line[1]
            s = Square(side)
            shapes.addShape(s)
        if line[0]=='circle':
            shape = line[0]
            radius = line[1]
            c = Circle(radius)
            shapes.addShape(c)
        if line[0] == 'triangle':
            share = line[0]
            base = line[1]
            height = line[2]
            t = Triangle(base,height)
            shapes.addShape(t)

    return shapes
        
##t = Triangle(6,6)
##c = Circle(1)
##ss = ShapeSet()
##ss.addShape(t)
##ss.addShape(c)
##largest = findLargest(ss)
##print largest
##print largest[0] is c

ss = readShapesFromFile('shapes.txt')
print ss
